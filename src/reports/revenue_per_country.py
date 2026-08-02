from collections import defaultdict

def revenue_per_country(events):
    revenue_dict = defaultdict(float)
    for event in events:
        revenue_dict[event.country] += event.revenue
    return revenue_dict



















