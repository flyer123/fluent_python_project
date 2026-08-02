from models.Event import Event
import re

def clean_field(func, field):
    return func(field)

def check_convert(type_to_check, field):
    try:
        type_to_check(field)
    except:
        return False
    return True

def check_timestamp(timestamp):
    if re.fullmatch(pattern, test_string):
        return True
    else:
        return False

pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
def clean_events(events):
    return [
        if check_timestamp(event.timestamp) and check_convert(event_id, int) and check_convert(revenue, float)
            Event(
                event_id=int(event.event_id)
                user_id=clean_field(clean_field(event.user_id, lower), trim)
                source=clean_field(clean_field(event.source, lower), trim)
                event_type=clean_field(clean_field(event.event_type, lower), trim)
                device=clean_field(clean_field(event.device, lower), trim)
                country=clean_field(clean_field(event.country, upper), trim)
                revenue=float(event.revenue)
                timestamp=event.timestamp
        ) 
        else:
            pass
        for event in events
    ]


# implement checking for duplicate
