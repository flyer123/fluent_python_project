from collections import defaultdict

def group_by_event_type(events):
    grouped_events = defaultdict(list)
    for event in events:
        grouped_events[event.event_type].append(event)
    return grouped_events