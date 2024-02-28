from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model and other necessary objects
with open('Maternals_pickle.pkl', 'rb') as file:
    model = pickle.load(file)

with open('LabelEncoder.pkl', 'rb') as file:
    le = pickle.load(file)

# Load the scaler used during training
with open('Scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            # If JSON data is received
            input_data = request.get_json()
        else:
            # If form data is received
            input_data = {
                'Age': float(request.form['Age']),
                'SystolicBP': float(request.form['SystolicBP']),
                'DiastolicBP': float(request.form['DiastolicBP']),
                'BS': float(request.form['BS']),
                'BodyTemp': float(request.form['BodyTemp']),
                'HeartRate': float(request.form['HeartRate'])
            }

        # Create a DataFrame with the input data
        input_df = pd.DataFrame(input_data, index=[0])

        # Normalize the input data using the saved scaler
        X_scaled = scaler.transform(input_df)

        # Make predictions
        prediction = model.predict(X_scaled)
        predicted_class = le.inverse_transform(prediction)[0]

        # Return the prediction as JSON response
        response = {'prediction': predicted_class}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
