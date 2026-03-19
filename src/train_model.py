"""
Hybrid Food Recommendation System - Training Pipeline
Trains both NLP and Metadata pipelines, then combines them
"""

import pandas as pd
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from nlp_pipeline import NLPPipeline
from metadata_pipeline import MetadataPipeline
from hybrid_scorer import HybridScorer

def train_hybrid_model():
    """Train both pipelines of the hybrid recommendation system"""
    
    print("=" * 60)
    print("HYBRID FOOD RECOMMENDATION SYSTEM - TRAINING")
    print("=" * 60)
    
    # Load data
    print("\n[1/4] Loading data...")
    df = pd.read_csv("data/food_data.csv")
    print(f"  ✓ Loaded {len(df)} food records")
    print(f"  ✓ Features: {', '.join(df.columns.tolist())}")
    
    # Train NLP Pipeline (Left side)
    print("\n[2/4] Training NLP Pipeline (Text embeddings + clustering)...")
    nlp_pipeline = NLPPipeline(n_clusters=3)
    nlp_pipeline.train(df)
    nlp_pipeline.save("models/nlp_pipeline.pkl")
    print("  ✓ NLP Pipeline trained and saved")
    print(f"    - Generated {len(df)} embeddings")
    print(f"    - Created {nlp_pipeline.n_clusters} food clusters")
    
    # Train Metadata Pipeline (Right side)
    print("\n[3/4] Training Metadata Pipeline (Structured classifier)...")
    metadata_pipeline = MetadataPipeline()
    metadata_pipeline.train(df)
    metadata_pipeline.save("models/metadata_pipeline.pkl")
    print("  ✓ Metadata Pipeline trained and saved")
    print(f"    - Classes: {', '.join(metadata_pipeline.classes)}")
    
    # Initialize Hybrid Scorer (Final stage)
    print("\n[4/4] Initializing Hybrid Scorer...")
    scorer = HybridScorer(nlp_weight=0.4, metadata_weight=0.6, confidence_threshold=0.5)
    print("  ✓ Hybrid Scorer initialized")
    print(f"    - NLP weight: {scorer.nlp_weight}")
    print(f"    - Metadata weight: {scorer.metadata_weight}")
    print(f"    - Confidence threshold: {scorer.confidence_threshold}")
    
    print("\n" + "=" * 60)
    print("✓ TRAINING COMPLETE")
    print("=" * 60)
    print("\nModel Summary:")
    print(f"  • NLP Pipeline: Text embeddings with {nlp_pipeline.n_clusters} clusters")
    print(f"  • Metadata Pipeline: Decision Tree classifier")
    print(f"  • Hybrid Scorer: Weighted combination of both pipelines")
    print(f"  • Food Database: {24} specific foods across 4 categories")
    print(f"  • Output: Specific food recommendations with details")
    print("\n✓ Models saved to models/ directory")
    print("✓ Ready for prediction!")

if __name__ == "__main__":
    train_hybrid_model()
