# 🍽️ Hybrid Food Recommendation System

A cutting-edge food recommendation engine using **dual parallel pipelines** that merge NLP embeddings with structured metadata classification.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   Food Recommendation Request                 │
│  (Mood, Diet, Weather, Hunger, Goal, Spice + Food Description)
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ┌────▼────────┐      ┌──────▼──────┐
    │ LEFT PIPELINE│      │RIGHT PIPELINE│
    │(NLP-based)   │      │(Metadata)    │
    └────┬────────┘      └──────┬──────┘
         │                      │
    [Text Embedding]    [Structured Data]
    [BERT Vectors]      [Classification]
    [Clustering]        [Probability Scores]
    [Similarity        [Food Category
     Scores]           Predictions]
         │                      │
         └───────────┬──────────┘
                     │
         ┌───────────▼──────────┐
         │  HYBRID SCORER        │
         │  Weighted Combination │
         │  Confidence Threshold │
         └───────────┬──────────┘
                     │
         ┌───────────▼──────────┐
         │ Final Recommendation  │
         │ with Confidence Score │
         └──────────────────────┘
```

## Key Components

### 1. **NLP Pipeline** (`nlp_pipeline.py`) - Left Side
Processes natural language food preferences:
- **Input**: Food descriptions/preferences (e.g., "Something light and healthy")
- **Processing**: 
  - Converts text to BERT embeddings
  - Clusters similar foods together
  - Calculates cosine similarity to all known foods
- **Output**: Similarity scores for each food category

### 2. **Metadata Pipeline** (`metadata_pipeline.py`) - Right Side
Processes structured user attributes:
- **Input**: Mood, time of day, hunger level, diet, weather, health goal, spice level
- **Processing**:
  - Encodes categorical features
  - Runs through trained Decision Tree classifier
  - Generates probability predictions for each food category
- **Output**: Classification confidence scores

### 3. **Hybrid Scorer** (`hybrid_scorer.py`) - Final Stage
Intelligently combines both pipeline outputs:
- **Weighted Combination**: Merges NLP and Metadata scores
  - Default weights: 40% NLP, 60% Metadata (tunable)
  - Normalized to 0-1 range
- **Confidence Thresholding**: Flags recommendations below threshold
- **Ranking**: Returns top K recommendations with confidence percentages

## How It Works

### Processing Flow

1. **Parallel Execution**:
   ```
   NLP Pipeline:     food_description → embeddings → similarities
   Metadata Pipeline: user_attributes → classification → probabilities
   ```

2. **Score Combination**:
   ```
   final_score = (0.4 × nlp_score) + (0.6 × metadata_score)
   ```

3. **Ranking & Filtering**:
   - Sort by final score descending
   - Flag if top score < confidence_threshold
   - Return top 3 recommendations

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

```bash
# Clone/Navigate to project
cd food_recommendation_system

# Install dependencies
pip install -r requirements.txt

# Download BERT model (one-time)
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

## Usage

### Training the Hybrid System

```bash
python src/train_model.py
```

Output:
- `models/nlp_pipeline.pkl` - Trained text embedding + clustering
- `models/metadata_pipeline.pkl` - Trained classifier
- Models are ready for prediction

### Running the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

### Programmatic Usage

```python
from src.predict import recommend_food_hybrid

# Get detailed recommendation with all pipeline outputs
result = recommend_food_hybrid(
    mood="happy",
    time_of_day="morning",
    hunger="medium",
    diet="veg",
    weather="hot",
    goal="weight_loss",
    spice="low",
    food_description="Light breakfast, something quick",
    return_details=True
)

print(result['top_recommendation'])  # "light meal"
print(result['confidence'])  # 0.84 (84% confidence)
print(result['recommendations'])  # List of top 3 with scores
print(result['nlp_scores'])  # Individual NLP pipeline scores
print(result['metadata_scores'])  # Individual metadata pipeline scores
```

## Configuration

### Adjusting Pipeline Weights

Edit in `predict.py` or programmatically:

```python
from src.hybrid_scorer import HybridScorer

scorer = HybridScorer(
    nlp_weight=0.5,           # More weight to text preferences
    metadata_weight=0.5,      # More weight to structured data
    confidence_threshold=0.6  # Require 60% confidence
)

scorer.set_weights(nlp_weight=0.3, metadata_weight=0.7)
scorer.set_threshold(0.55)
```

### Recommended Configurations

**Text-Focused** (User provides detailed food descriptions):
```
nlp_weight=0.6, metadata_weight=0.4
```

**Data-Focused** (Limited food description, trust structured preferences):
```
nlp_weight=0.3, metadata_weight=0.7
```

**Balanced** (Default):
```
nlp_weight=0.4, metadata_weight=0.6
```

## Example Interaction

**Input:**
```
Mood: stressed
Time: afternoon
Hunger: medium
Diet: veg
Weather: rainy
Goal: weight_loss
Spice: low
Description: "I want something comforting but healthy"
```

**Pipeline Outputs:**

NLP Pipeline (Text matching):
```
light meal:    0.75  (matches "healthy")
comfort food:  0.72  (matches "comforting")
snack:         0.50
heavy meal:    0.25
```

Metadata Pipeline (Preference classification):
```
light meal:    0.65
comfort food:  0.68
snack:         0.55
heavy meal:    0.12
```

**Hybrid Scores** (0.4 NLP + 0.6 Metadata):
```
comfort food:  0.70  ← TOP RECOMMENDATION (70% confidence)
light meal:    0.67
snack:         0.53
heavy meal:    0.17
```

## Model Details

### NLP Pipeline
- **Embedding Model**: SentenceTransformers (`all-MiniLM-L6-v2`)
  - 384-dimensional vectors
  - Pre-trained on semantic similarity
- **Clustering**: K-Means (3 clusters)
- **Similarity Metric**: Cosine similarity

### Metadata Pipeline
- **Classifier**: Decision Tree
  - Max depth: 10
  - Focus on interpretability
  - Handles categorical features
- **Encoding**: Label encoding for all features
- **Output**: Probability distribution over food categories

## Performance Considerations

### Parallel Execution
- Both pipelines process simultaneously
- NLP embedding: ~100ms (cached model)
- Metadata classification: ~1ms
- Scoring: <1ms
- **Total latency**: ~100ms per request

### Memory Usage
- Embedding model: ~60MB
- Trained pipelines: <1MB
- Active memory: ~150MB for pipeline execution

## Limitations & Future Improvements

### Current Limitations
1. **Limited training data** (24 samples) - can be expanded
2. **Pre-trained BERT** - not fine-tuned for food domain
3. **Simple metadata** - more features could improve accuracy
4. **Offline clustering** - clusters fixed at training time

### Future Enhancements
1. **More training data**: Expand dataset to 1000+ samples
2. **Fine-tuned BERT**: Train on food reviews and descriptions
3. **User feedback loop**: Incorporate preference learning
4. **Restaurant integration**: Add location and availability
5. **Nutritional information**: Include in recommendations
6. **Real-time clustering**: Dynamic cluster updates
7. **A/B testing framework**: Compare weight configurations
8. **Cold start handling**: For new users without history

## Testing

```python
# Quick validation
python -c "from src.predict import recommend_food; print(recommend_food('happy', 'morning', 'high', 'non-veg', 'hot', 'muscle_gain', 'high'))"
```

## Project Structure

```
food_recommendation_system/
├── app.py                      # Streamlit UI
├── requirements.txt            # Dependencies
├── data/
│   └── food_data.csv          # Training data
├── models/
│   ├── nlp_pipeline.pkl       # Trained NLP pipeline
│   └── metadata_pipeline.pkl  # Trained metadata pipeline
├── src/
│   ├── train_model.py         # Training script
│   ├── predict.py             # Prediction engine
│   ├── nlp_pipeline.py        # NLP pipeline class
│   ├── metadata_pipeline.py   # Metadata pipeline class
│   ├── hybrid_scorer.py       # Score combination logic
│   └── data_preprocessing.py  # Data utilities
└── outputs/
    └── evaluation.txt         # Results log
```

## Troubleshooting

### ImportError: No module named 'sentence_transformers'
```bash
pip install sentence-transformers
```

### CUDA/GPU Errors
The system falls back to CPU automatically. For GPU support:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Model Loading Error
Ensure models are trained first:
```bash
python src/train_model.py
```

## Contributing

To add improvements:
1. Expand `food_data.csv` with more training samples
2. Adjust weights in `src/predict.py` or `hybrid_scorer.py`
3. Fine-tune BERT model on your domain
4. Add new features to metadata

## License

MIT License - Feel free to use and modify!

---

**Built with ❤️ using Python, BERT, and scikit-learn**
