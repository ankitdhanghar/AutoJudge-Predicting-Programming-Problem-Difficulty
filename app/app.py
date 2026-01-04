from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
app = Flask(__name__)

tfidf = joblib.load('D:\\acm project\\models\\tfidf.pkl')
classifier = joblib.load("D:\\acm project\\models\\classifier.pkl")
regressor = joblib.load("D:\\acm project\\models\\regressor.pkl")
svd = joblib.load("D:\\acm project\\models\\svd.pkl")
scaler = joblib.load("D:\\acm project\\models\\scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        description = data.get("description", "")
        input_desc = data.get("input_description", "")
        output_desc = data.get("output_description", "")

        full_text = f"{description} {input_desc} {output_desc}".lower().strip()
        df = pd.DataFrame([full_text], columns = ["text"])

        X_text = tfidf.transform(df['text'])
        X_text = svd.transform(X_text)
        X_text = pd.DataFrame(X_text)
        #creating new features
        df['text_length'] = df['text'].apply(len)
        math_symbols = ["+", "-", "*", "/", "=", "<", ">"]
        def count_symbols(text):
             return sum(text.count(sym) for sym in math_symbols)
        df['math_symbols'] = df['text'].apply(count_symbols)
        keywords = ["graph", "dp", "recursion", "math", "string", "array", "greedy", "binarysearch"]
        for kw in keywords:
            df[f'{kw}_count'] = df["text"].str.lower().str.count(kw)
        X_text["text_length"] = df['text_length']
        X_text['math_symbols'] = df['math_symbols']
        for kw in keywords:
            X_text[f'{kw}_count'] = df[f'{kw}_count']
        X_text.columns = X_text.columns.astype(str)
        X_text['text_length'] = scaler.transform(X_text[['text_length']])

        difficulty_class = classifier.predict(X_text)[0]
        difficulty_score = regressor.predict(X_text)[0]
        
        return jsonify({
            "class": difficulty_class,
            "score": round(float(difficulty_score), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
