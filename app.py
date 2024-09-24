from flask import Flask, request,render_template, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

model = joblib.load('model/house_price_model.pkl')

# Route for the UI
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    
    square_footage = data.get('square_footage', None)
    bedrooms = data.get('bedrooms', None)
    bathrooms = data.get('bathrooms', None)

    # Validate input
    if square_footage is None or bedrooms is None or bathrooms is None:
        return jsonify({"error": "Missing one or more required fields: square_footage, bedrooms, bathrooms"}), 400

    # Perform prediction
    try:
        prediction = model.predict([[square_footage, bedrooms, bathrooms]])
        response = {
            'square_footage': square_footage,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'predicted_price': round(prediction[0], 2)
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8000)
