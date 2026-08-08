from models.Event import Event
import re

def check_timestamp(pattern, timestamp):
    if re.fullmatch(pattern, timestamp):
        return True
    else:
        return False


pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'

def check_for_empty_values(event):
    return any(not value for value in vars(event).values())


def validate_events(events):
    validated_events = []
    allowed_event_types = ["page_view", "purchase", "signup", "error", "login"]
    for event in events:
        if check_for_empty_values(event) == False and \
        check_timestamp(pattern, event.timestamp) == True and \
        event.revenue >= 0 and \
        event.event_type in allowed_event_types:
            validated_events.append(event)
    return validated_events

    
