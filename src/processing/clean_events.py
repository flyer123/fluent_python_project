from models.Event import Event
import re

def check_convert(field, type_to_check):
    try:
        type_to_check(field)
    except:
        return False
    return True

def check_timestamp(pattern, timestamp):
    if re.fullmatch(pattern, timestamp):
        return True
    else:
        return False


pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
def clean_events(events):
    event_ids=[]
    cleaned_events = []
    for event in events:
        if check_timestamp(pattern, event.timestamp) \
        and check_convert(event.event_id, int) \
        and check_convert(event.revenue, float) \
        and event.event_id not in event_ids:
            event = Event(
                event_id=int(event.event_id),
                user_id=event.user_id.lower().strip(),
                source=event.source.lower().strip(),
                event_type=event.event_type.lower().strip(),
                device=event.device.lower().strip(),
                country=event.country.upper().strip(),
                revenue=float(event.revenue),
                timestamp=event.timestamp
                ) 
            cleaned_events.append(event)
            event_ids.append(event.event_id)
        else:
            pass
    return cleaned_events



