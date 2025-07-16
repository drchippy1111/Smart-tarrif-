import pandas as pd
from modules import model

def test_predict_usage():
    usage_data = pd.DataFrame({'usage_gb': [1, 2, 3, 4]})
    prediction = model.predict_usage(usage_data)
    assert prediction > 0
