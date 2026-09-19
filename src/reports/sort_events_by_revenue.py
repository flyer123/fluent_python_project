from models.Event import Event

def sort_events_by_revenue(events: list[Event]) -> list[Event]:
    sorted_events = sorted(events, key=lambda x: x.revenue)
    return sorted_events