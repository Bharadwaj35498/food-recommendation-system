<<<<<<< HEAD
"""
Hybrid Food Recommendation System - Streamlit App
Uses parallel NLP + Metadata pipelines for intelligent recommendations
"""

=======
import pandas as pd
>>>>>>> 94253d4e6f8fea93b53532149ca9b3da953c26eb
import streamlit as st
from src.predict import recommend_food_hybrid

st.set_page_config(
<<<<<<< HEAD
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
=======
    page_title="Context-Aware Food Recommender",
    page_icon="🍽️",
    layout="wide",
)

st.title("🍽️ Context-Aware Food Recommender")
st.caption(
    "A context-first ML assistant that adapts food suggestions to your mood, "
    "schedule, cravings, and goals."
)

with st.sidebar:
    st.header("Your current context")
    mood = st.selectbox("Mood", ["happy", "tired", "stressed", "sad"])
    time = st.selectbox("Time of Day", ["morning", "afternoon", "night"])
    hunger = st.selectbox("Hunger Level", ["low", "medium", "high"])
    diet = st.selectbox("Diet Preference", ["veg", "non-veg"])
    weather = st.selectbox("Weather", ["hot", "cold", "rainy"])
    goal = st.selectbox("Health Goal", ["weight_loss", "muscle_gain", "maintenance"])
    spice = st.selectbox("Spice Level", ["low", "medium", "high"])
    st.divider()
    st.write("✅ Update your context and generate a recommendation.")
    recommend = st.button("Recommend Food", use_container_width=True)

left_col, right_col = st.columns([1.05, 1])

with left_col:
    st.subheader("Context snapshot")
    snapshot = {
        "Mood": mood.title(),
        "Time of Day": time.title(),
        "Hunger": hunger.title(),
        "Diet": "Vegetarian" if diet == "veg" else "Non-vegetarian",
        "Weather": weather.title(),
        "Health Goal": goal.replace("_", " ").title(),
        "Spice Level": spice.title(),
    }
    snapshot_df = pd.DataFrame(
        {"Signal": list(snapshot.keys()), "Selection": list(snapshot.values())}
    )
    st.table(snapshot_df)

    with st.expander("How this works"):
        st.markdown(
            """
            The model turns your context into encoded features, then predicts a food
            category using a decision tree. The probability chart helps explain which
            categories were most likely, and why the final recommendation was selected.
            """
        )

with right_col:
    st.subheader("Recommendation")
    if recommend:
        recommendation, probabilities = recommend_food(
            mood,
            time,
            hunger,
            diet,
            weather,
            goal,
            spice,
        )
        st.success(f"🍽️ Suggested category: **{recommendation}**")

        if probabilities:
            proba_series = pd.Series(probabilities).sort_values(ascending=False)
            st.metric(
                label="Confidence",
                value=f"{proba_series.iloc[0] * 100:.0f}%",
                delta=f"Top {len(proba_series)} categories ranked",
            )
            st.bar_chart(proba_series, height=240)
            st.write("Top alternatives")
            st.dataframe(
                proba_series.reset_index().rename(
                    columns={"index": "Category", 0: "Probability"}
                ),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("Confidence scores are not available for this model.")
    else:
        st.info("Select your context in the sidebar, then click **Recommend Food**.")
>>>>>>> 94253d4e6f8fea93b53532149ca9b3da953c26eb
