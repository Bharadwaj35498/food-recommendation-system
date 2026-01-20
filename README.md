# 🍽️ Context-Aware Food Recommendation System

A human-centric machine learning project that recommends food based on user mood, time of day, hunger level, diet preference, weather conditions, health goals, and spice tolerance.

This project demonstrates practical ML thinking by modeling how humans actually make food choices rather than focusing only on historical data.

---

## 🚀 Why This Project
People often struggle to decide what to eat, and their choices depend on context rather than fixed preferences.  
This system mimics real-life decision-making by incorporating multiple contextual factors into the recommendation process.

Example scenarios:
- Stressed + Night + Rainy → Comfort food  
- Morning + Weight loss goal → Light meal  

---

## 🧠 Machine Learning Approach

- Problem Type: Context-aware classification
- Model: Decision Tree Classifier
- Reason for model choice:
  - Handles categorical features well
  - Interpretable and explainable
  - Suitable for small and synthetic datasets

---

## 📊 Features Used

- Mood (happy, tired, stressed, sad)
- Time of Day (morning, afternoon, night)
- Hunger Level (low, medium, high)
- Diet Preference (veg / non-veg)
- Weather (hot, cold, rainy)
- Health Goal (weight loss, muscle gain, maintenance)
- Spice Level (low, medium, high)

---

## 🍽️ Output

- Food Category:
  - Light meal
  - Snack
  - Heavy meal
  - Comfort food

---

## 📈 Dataset Strategy

- Initial real dataset was limited
- Synthetic data was generated using rule-based heuristics to improve training stability
- Synthetic data is used only for prototyping purposes

---

## 🖥️ Application

The system is deployed as an interactive Streamlit web application where users can:
- Select contextual inputs via dropdowns
- Receive instant food recommendations
- Experience an end-to-end ML pipeline

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Git & GitHub

---

## 📁 Project Structure


food-recommendation-system/
├── src/
│ ├── data_preprocessing.py
│ ├── train_model.py
│ ├── predict.py
│ └── generate_synthetic_data.py
│
├── data/
│ └── food_data.csv
│
├── app.py
├── README.md
├── .gitignore
└── requirements.txt


---

## ▶️ How to Run the Project

```bash
git clone https://github.com/Bharadwaj35498/food-recommendation-system.git
cd food-recommendation-system

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python src/generate_synthetic_data.py
python src/train_model.py

streamlit run app.py
📌 Evaluation Notes

Accuracy varies due to limited real-world data

Focus is on feature engineering, context awareness, and ML workflow design

Model performance would improve with real user data

💼 What This Project Demonstrates

Solving real-life problems using machine learning

Context-aware feature engineering

Handling low-data scenarios

End-to-end ML pipeline development

Model deployment using Streamlit

Clean GitHub project structure

🔮 Future Enhancements

User history-based personalization

Calorie and nutrition estimation

Hybrid rule-based + ML recommendations

REST API deployment

Mobile-friendly interface
