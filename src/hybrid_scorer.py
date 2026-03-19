"""
Hybrid Scorer: Combines NLP and Metadata pipelines
Merges similarity scores from text embeddings with classification confidence
to produce final recommendation scores with thresholding
"""

import numpy as np
from typing import Dict, Tuple


class HybridScorer:
    """
    Combines outputs from both NLP and Metadata pipelines
    Produces final recommendation scores
    """
    
    def __init__(self, nlp_weight=0.4, metadata_weight=0.6, confidence_threshold=0.5):
        """
        Initialize hybrid scorer
        
        Args:
            nlp_weight: Weight for NLP pipeline output (0-1)
            metadata_weight: Weight for metadata pipeline output (0-1)
            confidence_threshold: Minimum confidence needed to recommend
        """
        self.nlp_weight = nlp_weight
        self.metadata_weight = metadata_weight
        self.confidence_threshold = confidence_threshold
        
        # Verify weights sum to 1
        total_weight = nlp_weight + metadata_weight
        if abs(total_weight - 1.0) > 0.001:
            raise ValueError(f"Weights must sum to 1.0, got {total_weight}")
    
    def score(self, 
              nlp_scores: Dict[str, float], 
              metadata_scores: Dict[str, float]) -> Dict[str, float]:
        """
        Combine NLP and Metadata scores
        
        Args:
            nlp_scores: Dict of food_category -> similarity_score from NLP pipeline
            metadata_scores: Dict of food_category -> probability from metadata pipeline
            
        Returns:
            dict: Food categories with final hybrid scores
        """
        # Get all unique food categories from both pipelines
        all_categories = set(nlp_scores.keys()) | set(metadata_scores.keys())
        
        hybrid_scores = {}
        
        for category in all_categories:
            # Get scores, defaulting to 0 if not present
            nlp_score = nlp_scores.get(category, 0.0)
            metadata_score = metadata_scores.get(category, 0.0)
            
            # Normalize scores to 0-1 range if needed
            nlp_score = max(0, min(1, nlp_score))
            metadata_score = max(0, min(1, metadata_score))
            
            # Weighted combination
            hybrid_score = (
                self.nlp_weight * nlp_score + 
                self.metadata_weight * metadata_score
            )
            
            hybrid_scores[category] = hybrid_score
        
        return hybrid_scores
    
    def get_recommendations(self,
                           nlp_scores: Dict[str, float],
                           metadata_scores: Dict[str, float],
                           top_k: int = 3) -> Dict:
        """
        Get ranked recommendations with confidence
        
        Args:
            nlp_scores: Scores from NLP pipeline
            metadata_scores: Scores from metadata pipeline
            top_k: Number of top recommendations to return
            
        Returns:
            dict with:
                - 'recommendations': List of top foods with scores
                - 'confidence': Overall confidence in top recommendation
                - 'needs_review': Bool if confidence below threshold
        """
        # Get hybrid scores
        hybrid_scores = self.score(nlp_scores, metadata_scores)
        
        # Sort by score
        sorted_recs = sorted(
            hybrid_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Get top K
        top_recommendations = sorted_recs[:top_k]
        
        # Check confidence
        top_score = top_recommendations[0][1] if top_recommendations else 0.0
        needs_review = top_score < self.confidence_threshold
        
        result = {
            'recommendations': [
                {
                    'food': food,
                    'score': float(score),
                    'confidence_pct': f"{score * 100:.1f}%"
                }
                for food, score in top_recommendations
            ],
            'confidence': float(top_score),
            'needs_review': needs_review,
            'threshold': self.confidence_threshold,
            'top_recommendation': top_recommendations[0][0] if top_recommendations else None
        }
        
        return result
    
    def set_weights(self, nlp_weight: float, metadata_weight: float):
        """
        Adjust pipeline weights
        
        Args:
            nlp_weight: New NLP weight
            metadata_weight: New metadata weight
            
        Raises:
            ValueError: If weights don't sum to 1.0
        """
        if abs(nlp_weight + metadata_weight - 1.0) > 0.001:
            raise ValueError(f"Weights must sum to 1.0")
        
        self.nlp_weight = nlp_weight
        self.metadata_weight = metadata_weight
    
    def set_threshold(self, threshold: float):
        """
        Set confidence threshold for recommendations
        
        Args:
            threshold: Confidence threshold (0-1)
        """
        if not 0 <= threshold <= 1:
            raise ValueError("Threshold must be between 0 and 1")
        
        self.confidence_threshold = threshold
