import pandas as pd
from modules import analyzer

def test_analyze_tariff():
    usage_data = pd.DataFrame({'usage_gb': [2, 3, 4]})
    plans = [
        {'name': 'Test Plan', 'data_limit': 5, 'price': 50}
    ]
    result = analyzer.analyze_tariff(usage_data, plans)
    assert result[0]['plan'] == 'Test Plan'
    assert 'estimated_cost' in result[0]
