import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data():
    df = pd.read_csv("data/food_data.csv")

    encoders = {}
    columns = [
        "mood", "time_of_day", "hunger_level",
        "diet", "weather", "health_goal", "spice_level",
        "food_category"
    ]

    for col in columns:
        encoders[col] = LabelEncoder()
        df[col + "_enc"] = encoders[col].fit_transform(df[col])

    X = df[
        [
            "mood_enc", "time_of_day_enc", "hunger_level_enc",
            "diet_enc", "weather_enc", "health_goal_enc", "spice_level_enc"
        ]
    ]

    y = df["food_category_enc"]

    return X, y, encoders
