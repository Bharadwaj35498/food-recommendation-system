import streamlit as st
from src.predict import recommend_food

st.title("🍽️ Food Recommendation System")

# Existing inputs
mood = st.selectbox("Mood", ["happy", "tired", "stressed", "sad"])
time = st.selectbox("Time of Day", ["morning", "afternoon", "night"])
hunger = st.selectbox("Hunger Level", ["low", "medium", "high"])
diet = st.selectbox("Diet Preference", ["veg", "non-veg"])

# 🔥 NEW inputs (these were missing)
weather = st.selectbox("Weather", ["hot", "cold", "rainy"])
goal = st.selectbox("Health Goal", ["weight_loss", "muscle_gain", "maintenance"])
spice = st.selectbox("Spice Level", ["low", "medium", "high"])

if st.button("Recommend Food"):
    result = recommend_food(
        mood,
        time,
        hunger,
        diet,
        weather,
        goal,
        spice
    )
    st.success(f"🍽️ Recommended Food: {result}")
