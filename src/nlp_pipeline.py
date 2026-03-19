"""
NLP Pipeline: Text embeddings and food clustering
Converts food descriptions to BERT embeddings and finds similar foods
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import joblib

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Warning: sentence-transformers not installed. Using dummy embeddings.")
    SentenceTransformer = None


class NLPPipeline:
    """
    Left pipeline: Handles food description text and generates embeddings
    """
    
    def __init__(self, model_name="all-MiniLM-L6-v2", n_clusters=5):
        """
        Initialize NLP pipeline with BERT-based embeddings
        
        Args:
            model_name: Sentence Transformers model
            n_clusters: Number of food clusters
        """
        if SentenceTransformer:
            self.embedding_model = SentenceTransformer(model_name)
        else:
            self.embedding_model = None
        
        self.n_clusters = n_clusters
        self.kmeans = None
        self.food_embeddings = None
        self.food_descriptions = None
        self.cluster_labels = None
        self.food_categories = None
    
    def train(self, df):
        """
        Train the NLP pipeline on food data
        
        Args:
            df: DataFrame with 'food_category' and 'food_description' columns
        """
        if self.embedding_model is None:
            # Fallback: use random embeddings for demo
            print("Using dummy embeddings (install sentence-transformers for real BERT)")
            np.random.seed(42)
            self.food_embeddings = np.random.randn(len(df), 384)
        else:
            # Generate embeddings for food descriptions
            descriptions = df["food_description"].tolist()
            self.food_embeddings = self.embedding_model.encode(
                descriptions, 
                convert_to_numpy=True
            )
        
        self.food_descriptions = df["food_description"].values
        self.food_categories = df["food_category"].values
        
        # Cluster similar foods
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)
        self.cluster_labels = self.kmeans.fit_predict(self.food_embeddings)
    
    def get_similarity_scores(self, query_text):
        """
        Find similar foods to a given text description
        
        Args:
            query_text: User query or food description
            
        Returns:
            dict: Food categories with similarity scores
        """
        if self.embedding_model is None:
            # Dummy embeddings
            query_embedding = np.random.randn(384)
        else:
            query_embedding = self.embedding_model.encode(query_text, convert_to_numpy=True)
        
        # Calculate similarity to all foods
        similarities = cosine_similarity(
            [query_embedding], 
            self.food_embeddings
        )[0]
        
        # Aggregate by food category
        category_scores = {}
        for category in np.unique(self.food_categories):
            mask = self.food_categories == category
            avg_similarity = similarities[mask].mean()
            category_scores[category] = float(avg_similarity)
        
        return category_scores
    
    def save(self, path="models/nlp_pipeline.pkl"):
        """Save the trained NLP pipeline"""
        joblib.dump(self, path)
    
    @staticmethod
    def load(path="models/nlp_pipeline.pkl"):
        """Load a trained NLP pipeline"""
        return joblib.load(path)
