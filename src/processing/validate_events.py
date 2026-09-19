from models.Event import Event
import re
import typing
from datetime import datetime, date



def check_for_empty_values(event: Event) -> typing.Any:
    """Check if any of Event object field is empty

    Args:
        event (Event): Event object to check

    Return:
        list of empty fields
    """
   
    return any(not value for value in vars(event).values())

def check_timestamp(timestamp: datetime) -> bool:
    """Check if datetime argument has valid value.
    If it has default value for January 1 1970 - check fails

    Args:
        timestamp (datetime): datetime field to check

    Return:
        True - if it has a valid value
        False - otherwise
    """
    if timestamp == datetime(1970, 1, 1, 1, 1):
        return True
    else:
        return False


def validate_events(events: list[Event]) -> list[Event]:
    """Validate fields of every object in events

    Args:
        events list(Event): list of Event objects to validate

    Return:
        list of Event objects that have valid values in their fields
    """
    validated_events = []
    allowed_event_types = ["page_view", "purchase", "signup", "error", "login"]
    for event in events:
        if check_for_empty_values(event) == False and \
        check_timestamp(event.timestamp) == False and \
        event.event_type in allowed_event_types:
            validated_events.append(event)
    return validated_events

    
