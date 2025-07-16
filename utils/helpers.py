def print_analysis(analysis):
    for item in analysis:
        print(f"Plan: {item['plan']}, Total Usage: {item['total_usage']}GB, Estimated Cost: ${item['estimated_cost']:.2f}")
