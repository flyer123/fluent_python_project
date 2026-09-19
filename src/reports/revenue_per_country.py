from collections import defaultdict
from models.Event import Event

def revenue_per_country(events: list[Event]) -> defaultdict[str, float]:
    revenue_dict: defaultdict[str, float] = defaultdict(float)
    for event in events:
        revenue_dict[event.country] += event.revenue
    return revenue_dict



















