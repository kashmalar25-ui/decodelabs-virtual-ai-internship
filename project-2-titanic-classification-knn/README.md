# Project 2: Titanic Survival Classification using KNN

A K-Nearest Neighbors classifier that predicts whether a Titanic passenger survived, using real historical passenger data from the Kaggle Titanic competition dataset.

## What went into it
- Cleaned and preprocessed 891 real passenger records
- Handled missing values (Age, Embarked) and encoded categorical features (Sex, Embarked)
- Feature scaling (critical for KNN's distance-based approach)
- Compared 6 different K values (1, 3, 5, 7, 9, 11) to find the best-performing one
- Trained + evaluated with a confusion matrix, classification report, and weighted F1 score
- Achieved a **weighted F1 score of 0.82**
- Built an interactive Streamlit demo so you can adjust a passenger's details (class, age, fare, sex, etc.) and see a live survival prediction

## Live Website Link
https://decodelabs-virtual-ai-internship-atgcpma6guujkuuwc3dlkm.streamlit.app/

## Files in this folder
- `Project2_Titanic_Survival_Classification.ipynb` — full notebook: data cleaning, model training, evaluation
- `app.py` — Streamlit web app for live predictions
- `requirements.txt` — Python packages needed to run the app
- `train.csv` — Titanic dataset (from Kaggle)

## How to run the notebook
Open the `.ipynb` file in Google Colab, upload `train.csv` to the session storage, and run all cells in order.

## How to run the app locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Self-verification against the project rubric
| Requirement | Status |
|---|---|
| Load and understand a dataset | Done |
| Split into training/testing sets | Done |
| Apply a classification algorithm | Done (KNN) |
| Data handling | Done (missing values, encoding, scaling) |
| Model training | Done |
| Output validation | Done (confusion matrix + F1 score) |
| Extra: K-value comparison | Done |
| Extra: Interactive web demo | Done (Streamlit) |

## What I learned
Working with real-world data required handling missing values and encoding categorical features before the model could use them — steps not needed with a clean textbook dataset. Comparing different K values showed how model choices directly affect performance, and building the Streamlit app taught me how to turn a trained model into something interactive that others can actually use and understand.

#AI #MachineLearning #Python #DataScience #DecodeLabs #Internship #LearnInPublic #KNN
