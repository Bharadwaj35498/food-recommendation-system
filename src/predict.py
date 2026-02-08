import joblib
import pandas as pd

model = joblib.load("models/food_model.pkl")
encoders = joblib.load("models/encoders.pkl")
food_labels = list(encoders["food_category"].classes_)


def build_input(mood, time_of_day, hunger, diet, weather, goal, spice):
    return pd.DataFrame(
        [[
            encoders["mood"].transform([mood])[0],
            encoders["time_of_day"].transform([time_of_day])[0],
            encoders["hunger_level"].transform([hunger])[0],
            encoders["diet"].transform([diet])[0],
            encoders["weather"].transform([weather])[0],
            encoders["health_goal"].transform([goal])[0],
            encoders["spice_level"].transform([spice])[0],
        ]],
        columns=[
            "mood_enc",
            "time_of_day_enc",
            "hunger_level_enc",
            "diet_enc",
            "weather_enc",
            "health_goal_enc",
            "spice_level_enc",
        ],
    )


def recommend_food(mood, time_of_day, hunger, diet, weather, goal, spice):
    input_data = build_input(mood, time_of_day, hunger, diet, weather, goal, spice)
    prediction = model.predict(input_data)
    recommendation = encoders["food_category"].inverse_transform(prediction)[0]

    probabilities = {}
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        probabilities = dict(zip(food_labels, proba))

    return recommendation, probabilities
