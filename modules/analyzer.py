def analyze_tariff(usage_data, plans):
    total_usage = usage_data['usage_gb'].sum()
    result = []
    for plan in plans:
        cost_per_gb = plan['price'] / plan['data_limit']
        overage = max(0, total_usage - plan['data_limit'])
        result.append({
            'plan': plan['name'],
            'total_usage': total_usage,
            'estimated_cost': plan['price'] + (cost_per_gb * overage)
        })
    return result
