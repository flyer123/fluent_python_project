def sort_events_by_revenue(events):
    sorted_events = sorted(events, key=lambda x: x.revenue)
    return sorted_events