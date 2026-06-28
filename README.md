# Stroke Prediction System

## Project Overview

The Stroke Prediction System is a Machine Learning web application developed using Python and Streamlit. It predicts whether a patient has a high or low risk of stroke based on their health information.

## Features

- Predicts stroke risk using a trained Machine Learning model.
- Simple and user-friendly interface.
- Built using Streamlit.
- Fast prediction results.

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Pickle

## Project Structure

```
Stroke_Prediction_App/
│
├── app.py
├── stroke_prediction_model.pkl
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/YourUsername/Stroke_Prediction_App.git
```

2. Open the project folder

```bash
cd Stroke_Prediction_App
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

## Input Features

The application takes the following inputs:

- Gender
- Age
- Hypertension
- Heart Disease
- Average Glucose Level
- BMI

*(Add any other features used by your model.)*

## Output

- Low Risk of Stroke
- High Risk of Stroke

## Author

**Tanuja Koritala**

## License

This project is developed for educational purposes.