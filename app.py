from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('fetal_health_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form.to_dict()

    # Convert to float
    input_values = [float(x) for x in input_data.values()]

    # Convert to DataFrame
    final_input = pd.DataFrame([input_values], columns=input_data.keys())

    prediction = model.predict(final_input)[0]

    # Convert result
    if prediction == 1:
        result = "Normal"
    elif prediction == 2:
        result = "Suspect"
    else:
        result = "Pathological"

    return render_template('index.html', prediction_text=f'Result: {result}')


if __name__ == "__main__":
    app.run(debug=True)