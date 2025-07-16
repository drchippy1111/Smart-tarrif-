def test_recommend_plan():
    analysis = [
        {'plan': 'A', 'estimated_cost': 50},
        {'plan': 'B', 'estimated_cost': 40}
    ]
    from modules import optimizer
    best = optimizer.recommend_plan(analysis)
    assert best['plan'] == 'B'
