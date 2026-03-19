# Quick Start Guide

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Core ML**: scikit-learn, numpy, pandas
- **NLP**: sentence-transformers (for BERT embeddings)
- **UI**: streamlit
- **Serialization**: joblib

## 2️⃣ Train the Hybrid System

```bash
python src/train_model.py
```

Output:
```
[1/4] Loading data...
[2/4] Training NLP Pipeline...
[3/4] Training Metadata Pipeline...
[4/4] Initializing Hybrid Scorer...
✓ TRAINING COMPLETE
```

This creates:
- `models/nlp_pipeline.pkl` - Text embedding + clustering
- `models/metadata_pipeline.pkl` - Structured classifier

## 3️⃣ Run the Demo (Optional)

```bash
python demo.py
```

See live examples of:
- How NLP pipeline scores text similarity
- How Metadata pipeline classifies preferences
- How the scores combine for final recommendations
- Different weight strategies
- Confidence threshold effects

## 4️⃣ Launch the Web App

```bash
streamlit run app.py
```

Then visit: `http://localhost:8501`

## 5️⃣ Make Predictions Programmatically

```python
from src.predict import recommend_food_hybrid

# Get detailed recommendation
result = recommend_food_hybrid(
    mood="happy",
    time_of_day="morning",
    hunger="medium",
    diet="veg",
    weather="hot",
    goal="weight_loss",
    spice="low",
    food_description="Something light and healthy",
    return_details=True
)

# Top recommendation
print(result['top_recommendation'])  # "light meal"
print(result['confidence'])  # 0.84

# See all alternatives
for rec in result['recommendations']:
    print(f"{rec['food']}: {rec['confidence_pct']}")

# Check pipeline scores
print("NLP Scores:", result['nlp_scores'])
print("Metadata Scores:", result['metadata_scores'])
```

---

## 🏗️ System Architecture Quick Reference

```
INPUT: User mood + preferences + food description
         ↓
    ┌────────────────────┐
    │  PARALLEL PIPELINES │
    └────┬───────────────┘
         ↓
    ┌────────────────────┐
    │  NLP Pipeline      │  ← BERT embeddings on text
    │  + Metadata        │  ← Classification on attributes
    └────┬───────────────┘
         ↓
    ┌────────────────────┐
    │  Hybrid Scorer     │  ← Weighted combination
    └────┬───────────────┘
         ↓
OUTPUT: Food recommendation + confidence score
```

## ⚙️ Configuration

Edit `config.py` to tune:

```python
# Pipeline weights (default 40% NLP, 60% Metadata)
NLP_PIPELINE_WEIGHT = 0.4
METADATA_PIPELINE_WEIGHT = 0.6

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.5

# Presets available
"text_focused"   → Emphasis on food descriptions (60% NLP)
"balanced"       → Equal emphasis (40% NLP, 60% Metadata)
"data_focused"   → Emphasis on mood/preferences (30% NLP)
```

## 🧪 Quick Test

```bash
# Check if everything is working
python -c "from src.predict import recommend_food; print(recommend_food('happy', 'morning', 'high', 'veg', 'hot', 'muscle_gain', 'high'))"
```

Expected output: A food category (e.g., "light meal", "heavy meal", "snack", "comfort food")

## 📊 Project Structure

```
food_recommendation_system/
├── app.py                      # Streamlit web interface
├── config.py                   # Configuration & presets
├── demo.py                     # Interactive demo
├── requirements.txt            # Dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # This file
├── data/
│   └── food_data.csv          # Training data (24 samples)
├── models/                     # Trained models (auto-created)
├── src/
│   ├── train_model.py         # Training script
│   ├── predict.py             # Prediction engine
│   ├── nlp_pipeline.py        # NLP component
│   ├── metadata_pipeline.py   # Metadata component
│   ├── hybrid_scorer.py       # Scoring component
│   └── data_preprocessing.py  # Utilities
└── outputs/                    # Results (auto-created)
```

## 🔧 Troubleshooting

### Q: ModuleNotFoundError
**A:** Run `pip install -r requirements.txt`

### Q: Models not found
**A:** Run `python src/train_model.py` first

### Q: BERT download fails
**A:** Fallback embeddings will be used automatically

### Q: Streamlit won't start
**A:** Try `pip install --upgrade streamlit`

## 📈 Next Steps

1. **Expand data**: Add more food samples to `data/food_data.csv`
2. **Fine-tune BERT**: Train on food-specific descriptions
3. **Add features**: Include nutrition info, cuisine type, cost
4. **Personalization**: Track user preferences over time
5. **Deployment**: Host on Heroku, AWS, or Azure

---

**All set! 🚀 Start with:**
```bash
python src/train_model.py && streamlit run app.py
```
