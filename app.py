from modules import data_collector, analyzer, optimizer, model, monitor
from utils.helpers import print_analysis

def main():
    usage_data = data_collector.collect_usage_data("data/usage_logs.csv")
    plans = data_collector.load_plans("data/plans.json")

    analysis = analyzer.analyze_tariff(usage_data, plans)
    print_analysis(analysis)

    best_plan = optimizer.recommend_plan(analysis)
    print("\nRecommended Plan:", best_plan['plan'])

    predicted = model.predict_usage(usage_data)
    print(f"\nPredicted Usage for Next Day: {predicted:.2f}GB")

    monitor.start_monitoring(usage_data, plans)

if __name__ == "__main__":
    main()
