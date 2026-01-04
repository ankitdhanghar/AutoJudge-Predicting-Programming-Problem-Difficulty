# AutoJudge-Predicting-Programming-Problem-Difficulty

## Project Overview
This project uses Natural Language Processing (NLP) and Machine Learning techniques to analyze programming problem statements and:
- Classify problems into difficulty levels
- Predict a numerical difficulty score

The system extracts text-based and structural features from problem descriptions and applies supervised learning models for both classification and regression. A web-based interface allows users to interactively test the trained models.

---


## Dataset Used
- File: `problems_data.jsonl`
- Format: JSON Lines
- Text fields:
  - `title`
  - `description`
  - `input_description`
  - `output_description`
- Target variables:
  - `problem_class` (classification)
  - `problem_score` (regression)

Missing values in text fields are handled by replacing them with empty strings.

---

## Approach and Models Used

### Data Preprocessing
- Combined all text fields into a single `full_text` column
- Converted text to lowercase
- Removed unnecessary special characters
- Missing values are filled with empty fields
- Scaling the features

### Feature Engineering
- TF-IDF Vectorization on `full_text`
- Truncated SVD for dimensionality reduction
- Additional handcrafted features:
  - Text length
  - Count of mathematical symbols (`+ - * / = < >`)
  - Keyword frequency (dp, graph, math, greedy, array, string)

### Models Used

#### Classification Models
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM) **(Best Performing Model)**

#### Regression Models
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor **(Best Performing Model)**

---

## Evaluation Metrics

### Classification
- Accuracy ~ 54%
- Confusion Matrix

### Regression
- Mean Absolute Error (MAE) ~1.71
- Root Mean Squared Error (RMSE) ~2.05
- R² Score~ 0.1170

---
## Steps to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ankitdhanghar/AutoJudge-Predicting-Programming-Problem-Difficulty.git
cd AutoJudge-Predicting-Programming-Problem-Difficulty
```
### 2. . Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```
### 3. Install Required Dependencies

Make sure Python (3.8+) is installed.

```bash
pip install streamlit scikit-learn pandas numpy scipy joblib
```
---

### 4. Add the Dataset

```bash
data/problems_data.jsonl
```
### Step 3: (Optional) Reproduce Model Training

If you want to retrain the models from scratch:

- Open AutoJudge_Model.ipynb
- Update base path according to your system like:
```bash
BASE_PATH = "/content/drive/MyDrive/ACM_Project"
```

- Run all cells sequentially
- Trained models will be saved inside the {BASE_PATH}/ directory

> Note: Changing paths is necessary because absolute paths depend on the local system.
---

### Step 4: Run the Flask Web Application

- Open app.py
- Update model paths to match your local directory structure, for example:

```bash

tfidf = joblib.load(r"{BASE_PATH}\tfidf.pkl")
```

- Run the app:

```bash
python app.py
```
---

### Step 5: Use the Application

- Paste problem description, input description, and output description
- Click Predict
- View predicted:
  - Difficulty Class (Easy / Medium / Hard)
  - Difficulty Score

##  Web Interface (Flask)

The web interface is built using **Flask** and provides a simple user workflow:

1. The interface contains three input text fields where users can enter:
   - Problem description
   - Input description
   - Output description

2. When the user clicks the **Predict** button:
   - The input text is sent to the Flask backend
   - The text is preprocessed using the same pipeline as the training phase
   - TF-IDF features and handcrafted features are generated
   - The trained classification and regression models are loaded

3. The application then displays:
   - Predicted difficulty class
   - Predicted difficulty score

The Flask application runs locally on `localhost` and does not require any database or cloud deployment.

## Author

**Ankit Dhanghar(23117023)** , IIT Roorkee


