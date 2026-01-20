import joblib
import pandas as pd

model = joblib.load("models/food_model.pkl")
encoders = joblib.load("models/encoders.pkl")

def recommend_food(mood, time_of_day, hunger, diet, weather, goal, spice):
    input_data = pd.DataFrame([[
        encoders["mood"].transform([mood])[0],
        encoders["time_of_day"].transform([time_of_day])[0],
        encoders["hunger_level"].transform([hunger])[0],
        encoders["diet"].transform([diet])[0],
        encoders["weather"].transform([weather])[0],
        encoders["health_goal"].transform([goal])[0],
        encoders["spice_level"].transform([spice])[0],
    ]], columns=[
        "mood_enc", "time_of_day_enc", "hunger_level_enc",
        "diet_enc", "weather_enc", "health_goal_enc", "spice_level_enc"
    ])

    pred = model.predict(input_data)
    return encoders["food_category"].inverse_transform(pred)[0]
