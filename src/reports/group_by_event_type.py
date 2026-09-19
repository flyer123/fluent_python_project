from collections import defaultdict
from models.Event import Event

def group_by_event_type(events: list[Event]) -> defaultdict[str, list[Event]]:
    grouped_events = defaultdict(list)
    for event in events:
        grouped_events[event.event_type].append(event)
    return grouped_events