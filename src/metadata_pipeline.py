"""
Metadata Pipeline: Structured classifier for food recommendations
Takes attributes like mood, time, hunger, diet, weather, goal, spice
and predicts food category with confidence scores
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib


class MetadataPipeline:
    """
    Right pipeline: Handles structured metadata and produces classification scores
    """
    
    def __init__(self):
        """Initialize metadata pipeline with classifier and encoders"""
        self.model = None
        self.encoders = {}
        self.feature_columns = [
            "mood",
            "time_of_day", 
            "hunger_level",
            "diet",
            "weather",
            "health_goal",
            "spice_level"
        ]
        self.target_column = "food_category"
        self.classes = None
    
    def train(self, df):
        """
        Train metadata classifier on structured data
        
        Args:
            df: DataFrame with mood, time_of_day, hunger_level, diet, weather, 
                health_goal, spice_level, and food_category columns
        """
        df_copy = df.copy()
        
        # Encode categorical features
        for col in self.feature_columns:
            self.encoders[col] = LabelEncoder()
            df_copy[col + "_enc"] = self.encoders[col].fit_transform(df_copy[col])
        
        # Encode target
        self.encoders[self.target_column] = LabelEncoder()
        df_copy[self.target_column + "_enc"] = self.encoders[self.target_column].fit_transform(
            df_copy[self.target_column]
        )
        
        self.classes = self.encoders[self.target_column].classes_
        
        # Prepare training data
        X = df_copy[[col + "_enc" for col in self.feature_columns]]
        y = df_copy[self.target_column + "_enc"]
        
        # Train classifier
        self.model = DecisionTreeClassifier(random_state=42, max_depth=10)
        self.model.fit(X, y)
        
        return self.model
    
    def predict_with_confidence(self, metadata_dict):
        """
        Get predictions with confidence scores for each food category
        
        Args:
            metadata_dict: Dict with mood, time_of_day, hunger_level, diet, 
                          weather, health_goal, spice_level
            
        Returns:
            dict: Food categories with probability scores
        """
        # Encode input
        input_data = []
        for col in self.feature_columns:
            encoded_value = self.encoders[col].transform([metadata_dict[col]])[0]
            input_data.append(encoded_value)
        
        input_array = np.array([input_data])
        
        # Get probability predictions for all classes
        proba = self.model.predict_proba(input_array)[0]
        
        # Map probabilities to food categories
        scores = {}
        for idx, category in enumerate(self.classes):
            scores[category] = float(proba[idx])
        
        return scores
    
    def predict(self, metadata_dict):
        """
        Get single top prediction
        
        Args:
            metadata_dict: Dict with metadata attributes
            
        Returns:
            str: Recommended food category
        """
        # Encode input
        input_data = []
        for col in self.feature_columns:
            encoded_value = self.encoders[col].transform([metadata_dict[col]])[0]
            input_data.append(encoded_value)
        
        input_array = np.array([input_data])
        pred_encoded = self.model.predict(input_array)[0]
        pred_category = self.encoders[self.target_column].inverse_transform([pred_encoded])[0]
        
        return pred_category
    
    def save(self, path="models/metadata_pipeline.pkl"):
        """Save the trained metadata pipeline"""
        joblib.dump(self, path)
    
    @staticmethod
    def load(path="models/metadata_pipeline.pkl"):
        """Load a trained metadata pipeline"""
        return joblib.load(path)
