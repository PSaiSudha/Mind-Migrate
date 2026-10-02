import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_and_save_model():
    # Simulated training dataset: [typing_speed_wpm, backspace_count, app_switch_freq]
    X = [
        [85, 2, 1],   # Focused
        [90, 1, 2],   # Focused
        [40, 15, 8],  # Stressed
        [35, 18, 10], # Stressed
        [50, 8, 5],   # Fatigued
        [45, 10, 6],  # Fatigued
        [70, 3, 3],   # Calm
        [75, 4, 2]    # Calm
    ]
    y = ["Focused", "Focused", "Stressed", "Stressed", "Fatigued", "Fatigued", "Calm", "Calm"]
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/mood_model.pkl")
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_and_save_model()