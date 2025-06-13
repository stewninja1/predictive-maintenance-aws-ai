import joblib
import pandas as pd

def predict_rul(sensor_data):
    model = joblib.load('rul_regression_model.pkl')
    return model.predict(sensor_data)[0]