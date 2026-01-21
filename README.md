Context-Aware Food Recommendation System

Overview

This project is a machine learning based food recommendation system that suggests food categories based on a person’s current context. Instead of relying on past user history, the system focuses on real-world factors that influence daily food decisions, such as mood, time of day, hunger level, weather, diet preference, health goals, and spice tolerance.

The goal of this project is to demonstrate practical machine learning concepts through a relatable problem and to build an end-to-end pipeline from data preparation to deployment.

Problem Statement

People often find it difficult to decide what to eat, especially when their choices depend on multiple situational factors. Food decisions are rarely random and are usually influenced by emotions, time, and lifestyle preferences. This project attempts to model that decision-making process using machine learning.

Approach

The problem is treated as a context-aware classification task. Multiple contextual features are encoded and used as inputs to a machine learning model that predicts an appropriate food category.

A Decision Tree classifier is used because it works well with categorical data and provides interpretable decision paths. The model learns relationships between different contexts and food choices.

Due to limited availability of real user data, synthetic data is generated using simple rule-based logic that reflects common human food preferences. This helps improve model stability and learning behavior while keeping the system realistic.

Features Used

The model considers the following contextual features.

Mood
Time of day
Hunger level
Diet preference
Weather conditions
Health goal
Spice preference

Output

Based on the input context, the system predicts one of the following food categories.

Light meal
Snack
Heavy meal
Comfort food

Technology Stack

The project is implemented using Python. Data processing and feature engineering are handled using Pandas and NumPy. Machine learning is implemented using scikit-learn. Joblib is used to save and load trained models and encoders. The application is deployed using Streamlit for interactive use. Git and GitHub are used for version control.

Project Structure

food-recommendation-system
src
data
app.py
README.md
requirements.txt

How to Run the Project

Clone the repository and navigate to the project directory. Create and activate a virtual environment. Install the required dependencies from the requirements file. Generate the dataset and train the model. Finally, run the Streamlit application to interact with the system.

Evaluation

Model accuracy varies due to the limited size of real-world data and the large number of possible input combinations. The primary focus of this project is on feature engineering, context awareness, and pipeline design rather than achieving high accuracy on a small dataset.

Use Case

This system can be used as a prototype for meal planning applications, food delivery platforms, or lifestyle recommendation systems. It demonstrates how contextual information can improve personalization in everyday applications.

Future Improvements

Future enhancements may include incorporating user history, calorie and nutrition analysis, hybrid rule-based and machine learning approaches, API deployment, and mobile application support.
