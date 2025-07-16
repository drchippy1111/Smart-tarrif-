from sklearn.linear_model import LinearRegression
import numpy as np

def predict_usage(usage_data):
    usage_data['day'] = range(len(usage_data))
    X = usage_data[['day']]
    y = usage_data['usage_gb']
    model = LinearRegression().fit(X, y)
    next_day = np.array([[len(usage_data)]])
    prediction = model.predict(next_day)
    return prediction[0]
