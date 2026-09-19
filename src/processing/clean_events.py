from models.Event import Event
from typing import Any





def clean_events(events: list[Event]) -> list[Event]:
    """Clean each object in events list:
    currently remove whitespaces at both ends of text fields and make them lower case.

    Args:
        events (list[Event]): list of Event to be cleaned

    Return:
        new list of cleaned objects of type Event
    """
    event_ids=[]
    cleaned_events = []
    for event in events:
        if event.event_id not in event_ids:
            event = Event(
                event_id=event.event_id,
                user_id=event.user_id.lower().strip(),
                source=event.source.lower().strip(),
                event_type=event.event_type.lower().strip(),
                device=event.device.lower().strip(),
                country=event.country.upper().strip(),
                revenue=event.revenue,
                timestamp=event.timestamp
                ) 
            cleaned_events.append(event)
            event_ids.append(event.event_id)
        else:
            pass
    return cleaned_events



