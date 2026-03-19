"""
Hybrid Prediction Engine
Runs both NLP and Metadata pipelines in parallel and combines results
"""

import pandas as pd
import sys
from pathlib import Path
from typing import Dict

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from nlp_pipeline import NLPPipeline
from metadata_pipeline import MetadataPipeline
from hybrid_scorer import HybridScorer
from food_database import get_food_suggestion, get_all_foods_for_category

# Load trained models
nlp_pipeline = NLPPipeline.load("models/nlp_pipeline.pkl")
metadata_pipeline = MetadataPipeline.load("models/metadata_pipeline.pkl")
scorer = HybridScorer(nlp_weight=0.4, metadata_weight=0.6, confidence_threshold=0.5)


def recommend_food_hybrid(
    mood: str,
    time_of_day: str,
    hunger: str,
    diet: str,
    weather: str,
    goal: str,
    spice: str,
    food_description: str = None,
    return_details: bool = False
) -> Dict:
    """
    Hybrid recommendation using parallel pipelines
    
    Args:
        mood: Current mood
        time_of_day: morning, afternoon, or night
        hunger: low, medium, or high
        diet: veg or non-veg
        weather: hot, cold, or rainy
        goal: weight_loss, muscle_gain, or maintenance
        spice: low, medium, or high
        food_description: Optional food description/preference text
        return_details: If True, return all pipeline outputs and scores
        
    Returns:
        dict: Recommendation with confidence scores and specific foods
    """
    
    # ===== LEFT PIPELINE: NLP =====
    nlp_scores = {}
    if food_description and food_description.strip():
        # Process text description
        nlp_scores = nlp_pipeline.get_similarity_scores(food_description)
    else:
        # If no description, give equal weight to all categories
        nlp_scores = {
            "light meal": 0.5,
            "heavy meal": 0.5,
            "snack": 0.5,
            "comfort food": 0.5
        }
    
    # ===== RIGHT PIPELINE: METADATA =====
    metadata_dict = {
        "mood": mood,
        "time_of_day": time_of_day,
        "hunger_level": hunger,
        "diet": diet,
        "weather": weather,
        "health_goal": goal,
        "spice_level": spice
    }
    metadata_scores = metadata_pipeline.predict_with_confidence(metadata_dict)
    
    # ===== FINAL STAGE: HYBRID SCORER =====
    recommendation = scorer.get_recommendations(
        nlp_scores, 
        metadata_scores,
        top_k=3
    )
    
    # ===== GET SPECIFIC FOOD SUGGESTIONS =====
    foods_with_details = []
    for rec in recommendation['recommendations']:
        category = rec['food']
        
        # Get a specific food from the category
        food_detail = get_food_suggestion(
            category=category,
            mood=mood,
            time_of_day=time_of_day,
            diet=diet
        )
        
        if food_detail:
            foods_with_details.append({
                'category': category,
                'food_name': food_detail['name'],
                'description': food_detail['description'],
                'prep_time': food_detail['prep_time'],
                'calories': food_detail['calories'],
                'score': rec['score'],
                'confidence_pct': rec['confidence_pct']
            })
    
    # Update recommendation with detailed foods
    recommendation['foods_detailed'] = foods_with_details
    recommendation['top_food_name'] = foods_with_details[0]['food_name'] if foods_with_details else None
    recommendation['top_food_description'] = foods_with_details[0]['description'] if foods_with_details else None
    
    if return_details:
        # Return all details for transparency
        recommendation['nlp_scores'] = nlp_scores
        recommendation['metadata_scores'] = metadata_scores
        recommendation['pipeline_weights'] = {
            'nlp': scorer.nlp_weight,
            'metadata': scorer.metadata_weight
        }
    
    return recommendation


def recommend_food(
    mood: str,
    time_of_day: str,
    hunger: str,
    diet: str,
    weather: str,
    goal: str,
    spice: str,
    food_description: str = None
) -> str:
    """
    Simple interface - returns just the top food name
    
    Args:
        mood: Current mood
        time_of_day: morning, afternoon, or night
        hunger: low, medium, or high
        diet: veg or non-veg
        weather: hot, cold, or rainy
        goal: weight_loss, muscle_gain, or maintenance
        spice: low, medium, or high
        food_description: Optional food description/preference text
        
    Returns:
        str: Recommended food name
    """
    rec = recommend_food_hybrid(
        mood=mood,
        time_of_day=time_of_day,
        hunger=hunger,
        diet=diet,
        weather=weather,
        goal=goal,
        spice=spice,
        food_description=food_description
    )
    return rec['top_food_name']
