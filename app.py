import pandas as pd
import streamlit as st
from src.predict import recommend_food

st.set_page_config(
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
