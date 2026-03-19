"""
Hybrid Food Recommendation System - Streamlit App
Uses parallel NLP + Metadata pipelines for intelligent recommendations
"""

import streamlit as st
from src.predict import recommend_food_hybrid

st.set_page_config(
    page_title="🍽️ Food Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Hybrid Food Recommendation System")

st.write("""
This system uses a **hybrid approach** with two parallel pipelines:
- **Left Pipeline (NLP)**: Analyzes food descriptions and finds similar foods
- **Right Pipeline (Metadata)**: Uses your mood, hunger, diet, and preferences
- **Final Stage**: Combines both signals for intelligent recommendations
""")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Your Preferences")
    mood = st.selectbox("Mood", ["happy", "tired", "stressed", "sad"])
    time = st.selectbox("Time of Day", ["morning", "afternoon", "night"])
    hunger = st.selectbox("Hunger Level", ["low", "medium", "high"])
    diet = st.selectbox("Diet Preference", ["veg", "non-veg"])

with col2:
    st.subheader("🌍 Context & Goals")
    weather = st.selectbox("Weather", ["hot", "cold", "rainy"])
    goal = st.selectbox("Health Goal", ["weight_loss", "muscle_gain", "maintenance"])
    spice = st.selectbox("Spice Level", ["low", "medium", "high"])

# NLP input - food description
st.subheader("🔤 Food Description (Optional)")
st.write("Describe what kind of food you're craving for more personalized recommendations:")
food_description = st.text_area(
    "What kind of food are you thinking about?",
    placeholder="e.g., 'Something light and healthy', 'Comfort food with protein', 'Quick snack'",
    height=80
)

# Recommendation button
if st.button("🚀 Get Recommendation", use_container_width=True):
    with st.spinner("Analyzing with hybrid pipelines..."):
        result = recommend_food_hybrid(
            mood=mood,
            time_of_day=time,
            hunger=hunger,
            diet=diet,
            weather=weather,
            goal=goal,
            spice=spice,
            food_description=food_description,
            return_details=True
        )
    
    # Display results
    st.divider()
    
    # Top recommendation with confidence
    st.subheader("🎯 Top Recommendation")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.success(f"### 🍽️ {result['top_food_name']}")
        st.info(result['top_food_description'])
    
    with col2:
        st.metric("Confidence Score", f"{result['confidence']*100:.1f}%")
    
    with col3:
        if result['needs_review']:
            st.warning(f"⚠️ Below {result['threshold']*100:.0f}% confidence")
        else:
            st.success("✅ High confidence")
    
    # Additional details about top food
    if result['foods_detailed']:
        food_detail = result['foods_detailed'][0]
        
        st.subheader("📊 Food Details")
        detail_cols = st.columns(3)
        
        with detail_cols[0]:
            st.metric("⏱️ Prep Time", food_detail['prep_time'])
        with detail_cols[1]:
            st.metric("🔥 Calories", food_detail['calories'])
        with detail_cols[2]:
            st.metric("📂 Category", food_detail['category'])
    
    # Alternative recommendations
    st.subheader("🍽️ More Options")
    
    if result['foods_detailed']:
        for idx, food in enumerate(result['foods_detailed'][1:], 1):
            with st.expander(f"Option {idx+1}: {food['food_name']} ({food['confidence_pct']})"):
                st.write(f"**Description**: {food['description']}")
                
                alt_cols = st.columns(3)
                with alt_cols[0]:
                    st.caption(f"⏱️ {food['prep_time']}")
                with alt_cols[1]:
                    st.caption(f"🔥 {food['calories']} cal")
                with alt_cols[2]:
                    st.caption(f"Category: {food['category']}")
                
                if food['score'] < 0.5:
                    st.info("💡 This may be worth trying if top choice doesn't appeal to you")
    
    # Pipeline breakdown
    with st.expander("🔍 Pipeline Details (Advanced)"):
        st.write("**How the recommendation was made:**")
        
        # Show pipeline weights
        col1, col2 = st.columns(2)
        with col1:
            st.metric("NLP Pipeline Weight", f"{result['pipeline_weights']['nlp']*100:.0f}%")
        with col2:
            st.metric("Metadata Pipeline Weight", f"{result['pipeline_weights']['metadata']*100:.0f}%")
        
        # Show individual scores
        st.write("**NLP Pipeline Scores** (Text similarity):")
        for food, score in sorted(result['nlp_scores'].items(), key=lambda x: x[1], reverse=True):
            bar = "█" * int(score * 20)
            st.write(f"  • {food:20} {score:.2f}  {bar}")
        
        st.write("**Metadata Pipeline Scores** (Your preferences):")
        for food, score in sorted(result['metadata_scores'].items(), key=lambda x: x[1], reverse=True):
            bar = "█" * int(score * 20)
            st.write(f"  • {food:20} {score:.2f}  {bar}")
        
        if food_description:
            st.info(f"📝 Your description: *'{food_description}'*")
    
    st.divider()
    st.write("💡 **Tip:** Add a food description to get more personalized recommendations using our NLP pipeline!")
