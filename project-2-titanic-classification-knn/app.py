"""
Titanic Survival Classifier - Interactive Demo
DecodeLabs Internship - Project 2
Made by: Kashmala Rizwan

A Streamlit web app that trains a KNN classifier on the Titanic dataset
and lets users adjust a passenger's details to see a live survival prediction.
"""

import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

st.set_page_config(page_title="Titanic Survival Classifier", page_icon="🚢")


# --- Load and prepare the data (cached so it only runs once) ---
@st.cache_resource
def load_and_train():
    csv_path = os.path.join(os.path.dirname(__file__), "train.csv")
    df = pd.read_csv(csv_path)

    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(X_train, y_train)

    return model, scaler, X.columns.tolist()


model, scaler, feature_names = load_and_train()

# --- Page title ---
st.title("🚢 Titanic Survival Classifier")
st.write(
    "Adjust a passenger's details below and see whether the model "
    "predicts they would have survived the Titanic disaster."
)

# --- User inputs ---
st.subheader("Passenger details")

pclass = st.selectbox("Passenger Class", options=[1, 2, 3], index=2,
                       help="1 = First class, 2 = Second class, 3 = Third class")
sex = st.radio("Sex", options=["Male", "Female"])
age = st.slider("Age", min_value=0, max_value=80, value=30)
sibsp = st.slider("Siblings / Spouses aboard", min_value=0, max_value=8, value=0)
parch = st.slider("Parents / Children aboard", min_value=0, max_value=6, value=0)
fare = st.slider("Fare paid ($)", min_value=0.0, max_value=520.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", options=["Southampton", "Cherbourg", "Queenstown"])

# --- Convert inputs into the format the model expects ---
sex_val = 0 if sex == "Male" else 1
embarked_val = {"Southampton": 0, "Cherbourg": 1, "Queenstown": 2}[embarked]

input_data = pd.DataFrame([{
    "Pclass": pclass,
    "Sex": sex_val,
    "Age": age,
    "SibSp": sibsp,
    "Parch": parch,
    "Fare": fare,
    "Embarked": embarked_val,
}])[feature_names]

input_scaled = scaler.transform(input_data)

# --- Predict ---
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    st.subheader("Prediction")
    if prediction == 1:
        st.success("🟢 Predicted: SURVIVED")
    else:
        st.error("🔴 Predicted: DID NOT SURVIVE")

    prob_df = pd.DataFrame({
        "Outcome": ["Did Not Survive", "Survived"],
        "Probability": probabilities
    }).set_index("Outcome")

    st.bar_chart(prob_df)
