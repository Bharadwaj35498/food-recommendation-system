# 🚀 Setup Guide for Windows

Since Python isn't in your PATH, here's how to set up the Hybrid Food Recommendation System:

## Option 1: Using Python from Microsoft Store (Recommended)

### Step 1: Install Python
```powershell
# Open PowerShell as Administrator and run:
winget install Python.Python
# Or go to: https://apps.microsoft.com/store/detail/python/9NRWMJP3717K
```

### Step 2: Verify Installation
```powershell
python --version
python -m pip --version
```

### Step 3: Install Dependencies
```powershell
cd c:\Users\strom\food_recommendation_system
python -m pip install -r requirements.txt
```

### Step 4: Train the Model
```powershell
python src/train_model.py
```

### Step 5: Run the App
```powershell
streamlit run app.py
```

---

## Option 2: Using Python from python.org (Traditional)

### Step 1: Download & Install
1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or later
3. **IMPORTANT**: Check **"Add Python to PATH"** during installation

### Step 2: Restart PowerShell
Close and reopen PowerShell for PATH changes to take effect

### Step 3: Install Dependencies
```powershell
cd c:\Users\strom\food_recommendation_system
pip install -r requirements.txt
```

### Step 4: Train & Run
```powershell
python src/train_model.py
streamlit run app.py
```

---

## Option 3: Using Anaconda (For Data Science)

### Step 1: Install Anaconda
https://www.anaconda.com/download

### Step 2: Create Environment
```powershell
conda create -n food-rec python=3.10
conda activate food-rec
```

### Step 3: Install Dependencies
```powershell
cd c:\Users\strom\food_recommendation_system
pip install -r requirements.txt
```

### Step 4: Train & Run
```powershell
python src/train_model.py
streamlit run app.py
```

---

## Troubleshooting

### Issue: "python is not recognized"
**Solution**: Python isn't in PATH. 
- Option A: Add manually in System Properties → Environment Variables
- Option B: Reinstall Python and check "Add Python to PATH"
- Option C: Use full path: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\python.exe src/train_model.py`

### Issue: pip install fails
```powershell
# Upgrade pip first:
python -m pip install --upgrade pip

# Then install requirements:
pip install -r requirements.txt
```

### Issue: sentence-transformers download fails
```powershell
# The system will fallback to random embeddings
# Check your internet connection and try again:
pip install --upgrade sentence-transformers
```

### Issue: streamlit command not found
```powershell
# Install streamlit explicitly:
pip install streamlit==1.32.0
```

---

## Quick Start (After Python is Working)

```powershell
# 1. Navigate to project
cd c:\Users\strom\food_recommendation_system

# 2. Install dependencies (one time)
pip install -r requirements.txt

# 3. Train the model
python src/train_model.py

# 4. Run the web app
streamlit run app.py

# 5. Open browser to http://localhost:8501
```

---

## Verifying Installation

```powershell
# Check Python
python --version        # Should be 3.8+

# Check pip
pip --version

# Check key packages
pip show scikit-learn
pip show sentence-transformers
pip show streamlit

# Test import
python -c "from src.predict import recommend_food; print('✓ Imports work!')"
```

---

## Project Ready!

Once Python is installed, your project structure is:

```
c:\Users\strom\food_recommendation_system\
├── app.py                    ← Run: streamlit run app.py
├── demo.py                   ← Run: python demo.py
├── src/
│   ├── train_model.py        ← Run: python src/train_model.py
│   ├── predict.py            ← Used by app/demo
│   ├── nlp_pipeline.py       ← NLP component
│   ├── metadata_pipeline.py  ← Metadata component
│   └── hybrid_scorer.py      ← Scoring component
├── data/
│   └── food_data.csv         ← Training data (24 samples)
├── models/                   ← Will contain trained models
├── requirements.txt          ← Dependencies
├── config.py                 ← Configuration
├── README.md                 ← Full documentation
└── QUICKSTART.md            ← This guide
```

---

## System Architecture (What You're Getting)

```
🍽️ HYBRID FOOD RECOMMENDATION SYSTEM
├── ⬅️ NLP PIPELINE (40% weight)
│   ├── BERT text embeddings
│   ├── Food description similarity
│   └── Semantic clustering
│
├── ➡️ METADATA PIPELINE (60% weight)
│   ├── Decision Tree classifier
│   ├── Mood/preference classification
│   └── Probability predictions
│
└── ⬆️ HYBRID SCORER
    ├── Weighted score combination
    ├── Confidence thresholding
    └── Ranked recommendations
```

---

## Next Steps

1. **Install Python** (use one of the options above)
2. **Run Training**: `python src/train_model.py`
3. **Launch App**: `streamlit run app.py`
4. **Try Demo**: `python demo.py`
5. **Expand Dataset**: Add more food samples to `data/food_data.csv`

---

## Support

- **Full README**: See [README.md](README.md)
- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md)
- **Configuration**: Edit [config.py](config.py)

**The system is fully built and ready to go! Just need Python.** ✨
