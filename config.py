"""
Configuration file for Hybrid Food Recommendation System
Adjust these parameters to tune the behavior of the recommendation engine
"""

# ============================================================================
# HYBRID SCORER CONFIGURATION
# ============================================================================

# Pipeline Weights (must sum to 1.0)
# Higher NLP weight = more emphasis on food descriptions
# Higher metadata weight = more emphasis on mood/preferences
NLP_PIPELINE_WEIGHT = 0.4
METADATA_PIPELINE_WEIGHT = 0.6

# Confidence threshold for recommendations (0.0 to 1.0)
# If top recommendation score is below this, system flags for review
CONFIDENCE_THRESHOLD = 0.5

# Number of alternative recommendations to return
TOP_K_RECOMMENDATIONS = 3

# ============================================================================
# NLP PIPELINE CONFIGURATION
# ============================================================================

# Sentence Transformer model to use for embeddings
# Options: 'all-MiniLM-L6-v2' (fast), 'all-mpnet-base-v2' (high quality)
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Number of clusters for food grouping
# Higher = more specific groups, Lower = broader categories
NUMBER_OF_CLUSTERS = 3

# ============================================================================
# METADATA PIPELINE CONFIGURATION
# ============================================================================

# Decision Tree max depth (higher = more complex, more overfitting risk)
TREE_MAX_DEPTH = 10

# Random seed for reproducibility
RANDOM_STATE = 42

# ============================================================================
# TRAINING DATA CONFIGURATION
# ============================================================================

# Path to training CSV
DATA_PATH = "data/food_data.csv"

# Column names for features and target
FEATURE_COLUMNS = [
    "mood",
    "time_of_day",
    "hunger_level",
    "diet",
    "weather",
    "health_goal",
    "spice_level"
]

TARGET_COLUMN = "food_category"
TEXT_COLUMN = "food_description"

# ============================================================================
# MODEL PATHS
# ============================================================================

NLP_PIPELINE_PATH = "models/nlp_pipeline.pkl"
METADATA_PIPELINE_PATH = "models/metadata_pipeline.pkl"

# ============================================================================
# STREAMLIT UI CONFIGURATION
# ============================================================================

# Page title and icon
APP_TITLE = "🍽️ Hybrid Food Recommendation System"
APP_ICON = "🍽️"

# Show advanced pipeline details in UI
SHOW_ADVANCED_DETAILS = True

# Show confidence score
SHOW_CONFIDENCE_SCORE = True

# ============================================================================
# LOGGING & OUTPUT CONFIGURATION
# ============================================================================

# Path for evaluation output
OUTPUT_PATH = "outputs/evaluation.txt"

# Log detailed prediction info
DETAILED_LOGGING = True


# ============================================================================
# WEIGHT PRESETS (for easy switching)
# ============================================================================

WEIGHT_PRESETS = {
    "text_focused": {
        "nlp_weight": 0.6,
        "metadata_weight": 0.4,
        "description": "More emphasis on food descriptions"
    },
    "balanced": {
        "nlp_weight": 0.4,
        "metadata_weight": 0.6,
        "description": "Balanced between text and metadata"
    },
    "data_focused": {
        "nlp_weight": 0.3,
        "metadata_weight": 0.7,
        "description": "More emphasis on mood/preferences"
    },
    "nlp_only": {
        "nlp_weight": 0.8,
        "metadata_weight": 0.2,
        "description": "Mostly NLP-based (requires descriptions)"
    },
    "metadata_only": {
        "nlp_weight": 0.1,
        "metadata_weight": 0.9,
        "description": "Mostly metadata-based (no description needed)"
    }
}


# ============================================================================
# THRESHOLD PRESETS
# ============================================================================

THRESHOLD_PRESETS = {
    "strict": 0.7,      # Only show high-confidence recommendations
    "moderate": 0.5,    # Default
    "lenient": 0.3,     # Show more alternatives
}


def get_weight_preset(preset_name: str) -> dict:
    """Get a preset weight configuration"""
    return WEIGHT_PRESETS.get(preset_name, WEIGHT_PRESETS["balanced"])


def get_threshold_preset(preset_name: str) -> float:
    """Get a preset confidence threshold"""
    return THRESHOLD_PRESETS.get(preset_name, THRESHOLD_PRESETS["moderate"])
