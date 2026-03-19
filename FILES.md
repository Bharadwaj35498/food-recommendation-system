# 📦 Project File Reference

Complete guide to all files in the Hybrid Food Recommendation System.

## Core Application Files

### `app.py` - Main Web Interface
- **Purpose**: Streamlit web application
- **What it does**: 
  - Accepts user input (mood, time, hunger, diet, weather, goal, spice)
  - Optionally accepts food description
  - Displays top recommendations with confidence scores
  - Shows pipeline breakdown in expandable section
- **How to run**: `streamlit run app.py`
- **Key features**: 
  - Beautiful UI with metrics and columns
  - Real-time recommendations
  - Transparent pipeline visualization

### `src/train_model.py` - Training Engine
- **Purpose**: Train both NLP and Metadata pipelines
- **What it does**:
  - Loads food_data.csv
  - Trains NLP pipeline (embeddings + clustering)
  - Trains Metadata pipeline (classifier)
  - Initializes Hybrid Scorer
  - Saves all models to models/ directory
- **How to run**: `python src/train_model.py`
- **Output**: 
  - `models/nlp_pipeline.pkl`
  - `models/metadata_pipeline.pkl`
- **Run frequency**: Once per dataset change

### `src/predict.py` - Prediction Engine
- **Purpose**: Make recommendations using both pipelines
- **Key functions**:
  - `recommend_food_hybrid()`: Full details with all scores
  - `recommend_food()`: Simple top recommendation
- **Used by**: app.py, demo.py
- **Note**: Auto-loads trained models on import

## Component Files

### `src/nlp_pipeline.py` - NLP Component
- **Purpose**: Text embedding and similarity scoring
- **Class**: `NLPPipeline`
- **Key methods**:
  - `train()`: Train embeddings and clustering
  - `get_similarity_scores()`: Get similarity for text input
  - `save()/load()`: Persist/load model
- **Uses**: sentence-transformers (BERT)
- **Output**: Dictionary of food → similarity score

### `src/metadata_pipeline.py` - Metadata Component
- **Purpose**: Structured data classification
- **Class**: `MetadataPipeline`
- **Key methods**:
  - `train()`: Train classifier on structured data
  - `predict_with_confidence()`: Get probability for each food
  - `predict()`: Get single top prediction
  - `save()/load()`: Persist/load model
- **Uses**: scikit-learn Decision Tree
- **Output**: Dictionary of food → probability score

### `src/hybrid_scorer.py` - Scoring Component
- **Purpose**: Combine NLP and Metadata scores
- **Class**: `HybridScorer`
- **Key methods**:
  - `score()`: Combine two score dictionaries
  - `get_recommendations()`: Get ranked recommendations
  - `set_weights()`: Adjust pipeline weights
  - `set_threshold()`: Adjust confidence threshold
- **Formula**: `final = (nlp_weight × nlp_scores) + (metadata_weight × metadata_scores)`
- **Output**: Ranked recommendations with confidence

### `src/data_preprocessing.py` - Utilities (Legacy)
- **Purpose**: Helper functions for data processing
- **Note**: Preserved from original system
- **Usage**: Can be extended for future preprocessing

## Configuration & Data

### `config.py` - Configuration Management
- **Purpose**: Central configuration hub
- **Contains**:
  - Pipeline weights (NLP: 0.4, Metadata: 0.6)
  - Confidence threshold (0.5)
  - Model paths
  - Embedding model name
  - Weight presets (text_focused, balanced, data_focused)
  - Threshold presets (strict, moderate, lenient)
- **How to use**: Import and override values
- **Edit this to**: Tune system behavior

### `data/food_data.csv` - Training Data
- **Format**: CSV with 24 rows
- **Columns**:
  - `mood`: happy, tired, stressed, sad
  - `time_of_day`: morning, afternoon, night
  - `hunger_level`: low, medium, high
  - `diet`: veg, non-veg
  - `weather`: hot, cold, rainy
  - `health_goal`: weight_loss, muscle_gain, maintenance
  - `spice_level`: low, medium, high
  - `food_category`: light meal, heavy meal, snack, comfort food
  - `food_description`: Text description of the food
- **Expandable**: Add rows to improve model accuracy
- **Format**: Must be UTF-8 encoded

## Documentation

### `README.md` - Main Documentation
- **Length**: Comprehensive (1000+ lines)
- **Covers**:
  - System architecture overview
  - How each pipeline works
  - Installation instructions
  - Usage examples (CLI and programmatic)
  - Configuration options
  - Performance details
  - Troubleshooting
  - Future improvements
- **Best for**: Complete understanding of the system

### `QUICKSTART.md` - Quick Start Guide
- **Length**: ~150 lines
- **Covers**:
  - Installation in 3 steps
  - Training and running app
  - Configuration basics
  - Troubleshooting
- **Best for**: Getting up and running fast

### `SETUP_WINDOWS.md` - Windows Setup
- **Length**: ~200 lines
- **Covers**:
  - Python installation options (3 methods)
  - Troubleshooting PATH issues
  - Dependency installation
  - Verification steps
- **Best for**: Windows users without Python

### `ARCHITECTURE.md` - Technical Deep Dive
- **Length**: ~600 lines
- **Covers**:
  - Detailed component architecture
  - Data flow diagrams
  - Mathematical formulas
  - Scalability analysis
  - Extension points
  - Performance benchmarks
- **Best for**: Developers extending the system

### `FILES.md` - This File
- **Purpose**: Navigation guide
- **Describes**: Every file's purpose and usage

## Demo & Testing

### `demo.py` - Interactive Demo
- **Purpose**: Show the system in action
- **What it does**:
  - Run 4 realistic scenarios
  - Show NLP pipeline output
  - Show Metadata pipeline output
  - Show Hybrid combining process
  - Compare different weight configurations
  - Show threshold sensitivity
- **How to run**: `python demo.py`
- **Output**: Colored visualization of pipeline flows
- **Duration**: ~5 seconds

## Models Directory

### `models/nlp_pipeline.pkl` - NLP Model (Generated)
- **Size**: ~60MB (model is cached from sentence-transformers)
- **Contains**: 
  - BERT embeddings
  - K-Means clustering
  - Food descriptions vectors
  - Cluster labels
- **Created by**: `train_model.py`
- **Life**: Replace when retraining on new data

### `models/metadata_pipeline.pkl` - Metadata Model (Generated)
- **Size**: <1MB
- **Contains**:
  - Decision Tree classifier
  - Label encoders for all features
  - Training metrics
- **Created by**: `train_model.py`
- **Life**: Replace when adding features

## Outputs Directory

### `outputs/evaluation.txt` - Results Log (Generated)
- **Purpose**: Store evaluation results
- **Format**: Text file with metrics
- **Auto-created**: Can be generated by extending train_model.py

## Requirements & Environment

### `requirements.txt` - Dependencies
- **Purpose**: Python package versions
- **Managed with**: pip
- **Install**: `pip install -r requirements.txt`
- **Key packages**:
  - scikit-learn: ML algorithms
  - pandas: Data manipulation
  - numpy: Numerical computing
  - sentence-transformers: BERT embeddings
  - torch: Deep learning (for BERT)
  - streamlit: Web UI
  - joblib: Model serialization

## Hidden/Auto-Generated Files

### `.venv/` or `venv/` - Virtual Environment (Optional)
- **Purpose**: Isolated Python environment
- **Create**: `python -m venv venv`
- **Activate**: `venv\Scripts\activate` (Windows)

### `__pycache__/` - Python Cache
- **Purpose**: Compiled Python files (speeds up loading)
- **Auto-generated**: Yes
- **Safe to delete**: Yes (will be regenerated)

### `.streamlit/` - Streamlit Config (Auto-created)
- **Purpose**: Streamlit settings
- **Location**: User home directory
- **Edit if needed**: Can add theme, options, etc.

## File Organization Best Practices

### Directory Structure
```
food_recommendation_system/                ← Root
├── Core Files
│   ├── app.py                            ← Start here!
│   ├── config.py
│   ├── requirements.txt
│   ├── demo.py
│
├── Source Code (src/)
│   ├── train_model.py                    ← Training
│   ├── predict.py                        ← Prediction
│   ├── nlp_pipeline.py                   ← NLP logic
│   ├── metadata_pipeline.py              ← Metadata logic
│   ├── hybrid_scorer.py                  ← Scoring logic
│   └── data_preprocessing.py             ← Utilities
│
├── Data (data/)
│   └── food_data.csv                     ← Training data
│
├── Models (models/)                      ← Generated
│   ├── nlp_pipeline.pkl
│   └── metadata_pipeline.pkl
│
├── Results (outputs/)                    ← Generated
│   └── evaluation.txt
│
└── Documentation
    ├── README.md                         ← Full guide
    ├── QUICKSTART.md                     ← Fast start
    ├── SETUP_WINDOWS.md                  ← Windows help
    ├── ARCHITECTURE.md                   ← Technical
    └── FILES.md                          ← This file
```

## Reading Guide

**First Time Setup?**
1. Read: QUICKSTART.md (5 min)
2. No Python? Read: SETUP_WINDOWS.md (10 min)
3. Run: `pip install -r requirements.txt`
4. Run: `python src/train_model.py`
5. Run: `streamlit run app.py`

**Want to Understand the System?**
1. Read: README.md (30 min)
2. Read: ARCHITECTURE.md (30 min)
3. Run: `python demo.py` (5 min)
4. Look at: src/ files (20 min)

**Want to Extend the System?**
1. Read: ARCHITECTURE.md (Extension Points section)
2. Edit: config.py (adjust parameters)
3. Edit: data/food_data.csv (add samples)
4. Run: src/train_model.py (retrain)
5. Look at: src/ files to add features

**Want to Deploy?**
1. Read: README.md (Future Improvements)
2. Create: Docker config
3. Create: CI/CD pipeline
4. Deploy to: Heroku, AWS, Azure, etc.

## File Modification Guidelines

### Safe to Edit:
- ✅ `config.py` - Settings only
- ✅ `data/food_data.csv` - Add rows
- ✅ Documentation files (.md)
- ✅ `app.py` - UI changes

### Careful Editing:
- ⚠️ `src/` files - Requires understanding
- ⚠️ `src/train_model.py` - Changes affect model training
- ⚠️ `requirements.txt` - Version conflicts possible

### Don't Edit:
- ❌ `models/` - Auto-generated
- ❌ `outputs/` - Auto-generated
- ❌ `__pycache__/` - Auto-generated

## Total Lines of Code by Component

| Component | Lines | Purpose |
|-----------|-------|---------|
| nlp_pipeline.py | ~120 | Text embeddings |
| metadata_pipeline.py | ~140 | Structured classification |
| hybrid_scorer.py | ~130 | Score combination |
| train_model.py | ~70 | Training script |
| predict.py | ~100 | Prediction engine |
| app.py | ~150 | Web interface |
| config.py | ~120 | Configuration |
| demo.py | ~250 | Interactive demo |
| **Total** | **~1000** | **Entire system** |

## Summary

- **Core logic**: 400 lines (3 components × ~130 lines)
- **Training/Prediction**: 170 lines
- **UI/Demo**: 400 lines
- **Config/Docs**: 200 lines
- **Total**: ~1000 lines of Python

Compact, maintainable, and fully documented! 🚀
