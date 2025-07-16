def recommend_plan(analysis):
    return min(analysis, key=lambda x: x['estimated_cost'])
