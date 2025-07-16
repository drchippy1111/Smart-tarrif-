from config import THRESHOLD_ALERT

def start_monitoring(usage_data, plans):
    current_usage = usage_data['usage_gb'].sum()
    for plan in plans:
        if current_usage >= plan['data_limit'] * THRESHOLD_ALERT:
            print(f"[ALERT] You have used {current_usage}GB out of {plan['data_limit']}GB in {plan['name']}")
