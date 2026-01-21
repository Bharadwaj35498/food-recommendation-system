# Context-Aware Food Recommendation System

## Overview
This project is a machine learning based food recommendation system that suggests food categories based on a user’s current context. Instead of relying on historical user data, the system focuses on real-world factors that influence daily food choices, such as mood, time of day, hunger level, weather conditions, diet preference, health goals, and spice tolerance.

The project is designed as an end-to-end machine learning pipeline, covering data preparation, feature engineering, model training, evaluation, and deployment through an interactive web application.

---

## Problem Statement
Food decisions are rarely random. People choose what to eat based on their emotional state, physical condition, time constraints, and lifestyle preferences. Traditional recommendation systems often ignore these contextual factors.

This project aims to model human-like decision-making by incorporating multiple situational features to generate meaningful and intuitive food recommendations.

---

## Machine Learning Approach
The problem is framed as a context-aware classification task. Each user interaction is represented as a combination of contextual features, and the model predicts a suitable food category.

A Decision Tree classifier is used due to its interpretability and effectiveness with categorical features. This makes the model suitable for explaining recommendations and handling structured contextual inputs.

Because real-world labeled data is limited for this prototype, synthetic data is generated using rule-based heuristics that reflect common human food preferences. This improves model stability while maintaining realistic behavior.

---

## Features
The model considers the following contextual inputs:

- Mood (happy, tired, stressed, sad)
- Time of day (morning, afternoon, night)
- Hunger level (low, medium, high)
- Diet preference (vegetarian, non-vegetarian)
- Weather conditions (hot, cold, rainy)
- Health goal (weight loss, muscle gain, maintenance)
- Spice preference (low, medium, high)

---

## Output
Based on the input context, the system predicts one of the following food categories:

- Light meal
- Snack
- Heavy meal
- Comfort food

---

## Technology Stack
- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git and GitHub

---

## Project Structure
food-recommendation-system/
├── src/
│ ├── data_preprocessing.py
│ ├── train_model.py
│ ├── predict.py
│ └── generate_synthetic_data.py
├── data/
│ └── food_data.csv
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
---

## How to Run the Project

### 1. Clone the repository
git clone https://github.com/Bharadwaj35498/food-recommendation-system.git
cd food-recommendation-system
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Generate data and train the model
python src/generate_synthetic_data.py
python src/train_model.py
5. Run the Streamlit application
streamlit run app.py
Evaluation Notes
Model accuracy varies due to the limited size of real-world data and the large number of possible contextual combinations. The primary objective of this project is to demonstrate feature engineering, context-aware modeling, and end-to-end system design rather than optimizing accuracy on a small dataset.

Use Cases:-
Meal planning applications

Food delivery personalization

Lifestyle and wellness recommendation systems

Future Improvements:-
Incorporating user history for personalized recommendations

Adding calorie and nutritional analysis

Hybrid rule-based and machine learning approaches

REST API deployment

Mobile application integration
