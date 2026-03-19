"""
Demo script: Show the Hybrid Food Recommendation System in action
Run this to see how the two parallel pipelines work and combine their outputs
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from predict import recommend_food_hybrid, recommend_food
from hybrid_scorer import HybridScorer
import config


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_section(title):
    """Print formatted section"""
    print(f"\n  {title}")
    print("  " + "-" * 60)


def demo_scenario(scenario_name, mood, time_of_day, hunger, diet, weather, goal, spice, description=None):
    """Run a demo scenario and show all pipeline outputs"""
    
    print_header(f"SCENARIO: {scenario_name}")
    
    print("\n📋 INPUT:")
    print(f"  • Mood: {mood}")
    print(f"  • Time: {time_of_day}")
    print(f"  • Hunger: {hunger}")
    print(f"  • Diet: {diet}")
    print(f"  • Weather: {weather}")
    print(f"  • Goal: {goal}")
    print(f"  • Spice: {spice}")
    if description:
        print(f"  • Description: \"{description}\"")
    else:
        print(f"  • Description: (none)")
    
    # Get recommendation with full details
    result = recommend_food_hybrid(
        mood=mood,
        time_of_day=time_of_day,
        hunger=hunger,
        diet=diet,
        weather=weather,
        goal=goal,
        spice=spice,
        food_description=description,
        return_details=True
    )
    
    # Display pipeline outputs
    print_section("⬅️ NLP PIPELINE (Text Similarity)")
    for food, score in sorted(result['nlp_scores'].items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(score * 40)
        print(f"  {food:20} {score:.2f}  {bar}")
    
    print_section("➡️ METADATA PIPELINE (Classification)")
    for food, score in sorted(result['metadata_scores'].items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(score * 40)
        print(f"  {food:20} {score:.2f}  {bar}")
    
    print_section("⬆️ HYBRID SCORING (Combined Output)")
    print(f"  Weights: {result['pipeline_weights']['nlp']*100:.0f}% NLP + {result['pipeline_weights']['metadata']*100:.0f}% Metadata")
    for rec in result['recommendations']:
        bar = "█" * int(rec['score'] * 40)
        confidence = "✅" if not result['needs_review'] else "⚠️"
        print(f"  {rec['food']:20} {rec['score']:.2f}  {bar}  {confidence}")
    
    print_section("🎯 FINAL RECOMMENDATION")
    print(f"  Food: {result['top_food_name']}")
    print(f"  Description: {result['top_food_description']}")
    print(f"  Confidence: {result['confidence']*100:.1f}%")
    
    # Show detailed food info
    if result.get('foods_detailed'):
        food = result['foods_detailed'][0]
        print(f"\n  📊 Details:")
        print(f"    • Prep Time: {food['prep_time']}")
        print(f"    • Calories: {food['calories']}")
        print(f"    • Category: {food['category']}")
    
    if result['needs_review']:
        print(f"  Status: ⚠️ Below threshold ({result['threshold']*100:.0f}%) - Consider alternatives")
    else:
        print(f"  Status: ✅ High confidence - Safe to recommend")
    
    # Show alternatives
    if result.get('foods_detailed') and len(result['foods_detailed']) > 1:
        print(f"\n  🍽️ Alternative Options:")
        for idx, alt_food in enumerate(result['foods_detailed'][1:], 1):
            print(f"    {idx+1}. {alt_food['food_name']} ({alt_food['confidence_pct']})")
            print(f"       ⏱️  {alt_food['prep_time']} | 🔥 {alt_food['calories']}")


def demo_weight_comparison():
    """Show how different weights affect recommendations"""
    
    print_header("WEIGHT COMPARISON: Happy Morning with Description")
    
    description = "Something energizing and healthy for breakfast"
    
    # Get NLP scores
    from nlp_pipeline import NLPPipeline
    nlp = NLPPipeline.load("models/nlp_pipeline.pkl")
    nlp_scores = nlp.get_similarity_scores(description)
    
    # Get metadata scores
    from metadata_pipeline import MetadataPipeline
    metadata = MetadataPipeline.load("models/metadata_pipeline.pkl")
    metadata_scores = metadata.predict_with_confidence({
        "mood": "happy",
        "time_of_day": "morning",
        "hunger_level": "medium",
        "diet": "veg",
        "weather": "hot",
        "health_goal": "muscle_gain",
        "spice_level": "low"
    })
    
    print("\n📊 COMPARING DIFFERENT WEIGHT CONFIGURATIONS:\n")
    
    for preset_name, preset in config.WEIGHT_PRESETS.items():
        scorer = HybridScorer(
            nlp_weight=preset['nlp_weight'],
            metadata_weight=preset['metadata_weight']
        )
        
        result = scorer.get_recommendations(nlp_scores, metadata_scores)
        top_food = result['top_recommendation']
        score = result['confidence']
        
        print(f"  {preset_name:20} ({preset['nlp_weight']:.0%} NLP, {preset['metadata_weight']:.0%} Metadata)")
        print(f"    → Recommendation: {top_food:20} ({score:.1%} confidence)")
        print()


def demo_threshold_sensitivity():
    """Show how confidence threshold affects recommendations"""
    
    print_header("THRESHOLD SENSITIVITY ANALYSIS")
    
    # Use stressed evening mood
    from metadata_pipeline import MetadataPipeline
    metadata = MetadataPipeline.load("models/metadata_pipeline.pkl")
    metadata_scores = metadata.predict_with_confidence({
        "mood": "stressed",
        "time_of_day": "night",
        "hunger_level": "high",
        "diet": "veg",
        "weather": "rainy",
        "health_goal": "maintenance",
        "spice_level": "high"
    })
    
    from nlp_pipeline import NLPPipeline
    nlp = NLPPipeline.load("models/nlp_pipeline.pkl")
    nlp_scores = nlp.get_similarity_scores("comfort food")
    
    print("\n🎚️ CONFIDENCE THRESHOLD EFFECTS:\n")
    
    for threshold_name, threshold_value in config.THRESHOLD_PRESETS.items():
        scorer = HybridScorer(
            nlp_weight=0.4,
            metadata_weight=0.6,
            confidence_threshold=threshold_value
        )
        
        result = scorer.get_recommendations(nlp_scores, metadata_scores)
        status = "✅ Approved" if not result['needs_review'] else "⚠️ Needs Review"
        
        print(f"  {threshold_name:15} (threshold: {threshold_value:.0%})")
        print(f"    → {result['top_recommendation']:20} ({result['confidence']:.1%})  {status}")
        print()


def main():
    """Run all demos"""
    
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "🍽️ HYBRID FOOD RECOMMENDATION SYSTEM - DEMO" + " " * 14 + "║")
    print("╚" + "═" * 68 + "╝")
    
    print("\nThis demo shows how the hybrid system works:")
    print("  • LEFT PIPELINE (NLP): Processes food descriptions")
    print("  • RIGHT PIPELINE (Metadata): Uses mood/preferences")
    print("  • FINAL STAGE: Combines both for smart recommendations")
    
    # ===== SCENARIO 1: Happy morning
    demo_scenario(
        "Happy Morning - Wants Quick Energy",
        mood="happy",
        time_of_day="morning",
        hunger="medium",
        diet="non-veg",
        weather="hot",
        goal="muscle_gain",
        spice="low",
        description="Something quick and protein-packed"
    )
    
    # ===== SCENARIO 2: Stressed evening
    demo_scenario(
        "Stressed Evening - Wants Comfort",
        mood="stressed",
        time_of_day="night",
        hunger="high",
        diet="veg",
        weather="rainy",
        goal="maintenance",
        spice="high",
        description="Comfort food - something warm and filling"
    )
    
    # ===== SCENARIO 3: Sad afternoon - no description
    demo_scenario(
        "Sad Afternoon - No Food Description",
        mood="sad",
        time_of_day="afternoon",
        hunger="medium",
        diet="veg",
        weather="rainy",
        goal="maintenance",
        spice="medium",
        description=None
    )
    
    # ===== SCENARIO 4: Tired morning - health focus
    demo_scenario(
        "Tired Morning - Weight Loss Goal",
        mood="tired",
        time_of_day="morning",
        hunger="low",
        diet="veg",
        weather="cold",
        goal="weight_loss",
        spice="low",
        description="Light, healthy breakfast that won't make me feel heavy"
    )
    
    # ===== Weight comparison
    demo_weight_comparison()
    
    # ===== Threshold sensitivity
    demo_threshold_sensitivity()
    
    # ===== Summary
    print_header("SYSTEM SUMMARY")
    print("""
  The hybrid system successfully combines:
  
  ✓ NLP Pipeline (~40% weight):
    - Analyzes food descriptions with BERT embeddings
    - Finds semantically similar foods
    - Provides semantic understanding
  
  ✓ Metadata Pipeline (~60% weight):
    - Processes structured user attributes
    - Predicts preferences based on mood/context
    - Provides interpretable decisions
  
  ✓ Hybrid Scoring:
    - Weighted combination of both signals
    - Confidence-based filtering
    - Alternative recommendations
  
  🎯 Result: Intelligent, comprehensive food recommendations!
    """)
    
    print("=" * 70)
    print("\n✅ Demo complete! Now run the app:")
    print("     streamlit run app.py\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you've trained the models first:")
        print("   python src/train_model.py")
