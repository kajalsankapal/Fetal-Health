# Fetal AI

Fetal AI is a Flask-based machine learning web application for predicting fetal health from cardiotocography (CTG) related input features. The project loads a pre-trained model from `fetal_health_model.pkl` and classifies a case into one of three categories:

- `Normal`
- `Suspect`
- `Pathological`

## Web Interface
<img width="1568" height="906" alt="image" src="https://github.com/user-attachments/assets/6df96e03-d91d-459b-a5d7-d8185f5aca69" />
<img width="1594" height="905" alt="image" src="https://github.com/user-attachments/assets/fdfdad0c-5c45-4014-a4a0-e6f5874ef9f5" />
<img width="1551" height="901" alt="image" src="https://github.com/user-attachments/assets/6c4bae01-0ab0-42aa-a80d-6813c435f33d" />
<img width="1562" height="897" alt="image" src="https://github.com/user-attachments/assets/1da97f41-b10a-4e4c-8662-03d63d39a3e1" />
<img width="1563" height="896" alt="image" src="https://github.com/user-attachments/assets/bed8abfd-5ab8-4a0f-8deb-88f3860b6a8c" />

## Project Overview

This project includes:

- A trained machine learning model saved as `fetal_health_model.pkl`
- A Flask web app for user interaction
- HTML templates for home, about, contact, and prediction input pages
- Static assets such as CSS and images
- A dataset file `fetal_health.csv`
- Notebook and PDF files related to the project work

## Features

- Predict fetal health from 8 numeric medical input values
- Simple Flask web interface
- Pre-trained model loaded with `pickle`
- Prediction result displayed on the home page
- Additional informational pages like About and Contact

## Input Features

The application currently expects these fields:

1. `baseline value`
2. `accelerations`
3. `fetal_movement`
4. `uterine_contractions`
5. `light_decelerations`
6. `severe_decelerations`
7. `prolongued_decelerations`
8. `abnormal_short_term_variability`

## Tech Stack

- Python
- Flask
- Pandas
- Pickle
- HTML/CSS

## Project Structure

```text
FetalAI/
|-- README.md
|-- FetalAI.ipynb
|-- FetalAI.pdf
|-- fetal_health.csv
|-- fetal_health_model.pkl
|-- flask/
|   |-- app.py
|   |-- static/
|   |   |-- style.css
|   |   |-- hero-fetal.svg
|   |   |-- about-fetal.svg
|   |   `-- Images/
|   `-- templates/
|       |-- index.html
|       |-- input.html
|       |-- about.html
|       |-- contact.html
|       `-- images.html
```

## Installation

1. Clone or download the project.
2. Open a terminal in the project root.
3. Create and activate a virtual environment.
4. Install the required packages:

```bash
pip install flask pandas
```

## How to Run

From the project root, run:

```bash
python flask/app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Available Routes

- `/` - Home page
- `/about` - About the project
- `/contact` - Contact page
- `/input` - Input form for prediction
- `/images` - Placeholder gallery page
- `/predict` - POST route used to generate predictions

## Prediction Output

After submitting the form, the model returns one of the following classes:

- `1` -> `Normal`
- `2` -> `Suspect`
- `3` -> `Pathological`

## Notes

- The model file must remain in the project root as `fetal_health_model.pkl`.
- The Flask app is currently started in debug mode.
- All form values are converted to floating-point numbers before prediction.

## Future Improvements

- Add validation and user-friendly error handling for invalid inputs
- Add a proper image gallery to the Images page
- Add a `requirements.txt` file
- Improve contact form functionality
- Deploy the application online

## Author
Kajal Sankapal
AIML Student
