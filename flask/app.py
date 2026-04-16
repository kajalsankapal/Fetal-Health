from pathlib import Path
import pickle

import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
MODEL_PATH = PROJECT_ROOT / "fetal_health_model.pkl"
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = Flask(
    __name__,
    template_folder=str(TEMPLATES_DIR),
    static_folder=str(STATIC_DIR),
)

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)

FEATURE_FIELDS = [
    "baseline value",
    "accelerations",
    "fetal_movement",
    "uterine_contractions",
    "light_decelerations",
    "severe_decelerations",
    "prolongued_decelerations",
    "abnormal_short_term_variability",
]

CONTACT_DETAILS = {
    "location": [
        "Survey no. 91, Sundarayya Vignan Kendram,",
        "Technical Block, 6th floor, Madhava Reddy Colony,",
        "Gachibowli, Hyderabad, Telangana 500032",
    ],
    "email": "info@thesmartbridge.com",
    "call": "+91 6304320044",
}


def render_home(prediction_text=None):
    return render_template("index.html", prediction_text=prediction_text)


@app.route("/")
def home():
    return render_home()


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", contact=CONTACT_DETAILS)


@app.route("/input")
def input_page():
    return render_template("input.html", feature_fields=FEATURE_FIELDS)


@app.route("/images")
def images():
    return render_template("images.html")


@app.route("/predict", methods=["POST"])
def predict():
    input_values = []
    for field in FEATURE_FIELDS:
        raw_value = request.form.get(field, "").strip()
        input_values.append(float(raw_value))

    final_input = pd.DataFrame([input_values], columns=FEATURE_FIELDS)

    prediction = model.predict(final_input)[0]

    if prediction == 1:
        result = "Normal"
    elif prediction == 2:
        result = "Suspect"
    else:
        result = "Pathological"

    return render_home(prediction_text=f"fetal_health:{result}")


if __name__ == "__main__":
    app.run(debug=True)
