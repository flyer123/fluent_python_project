from models.Event import Event
from models.EnrichedEvent import EnrichedEvent


def enrich_events(events: list[Event]) -> list[EnrichedEvent]:
    """ Create list of EnrichedEvent objects

    Args:
        events: list of Event objects to create a new sequence

    Return:
        list of EnrichedEvent objects
    """
    return [EnrichedEvent.from_event(e) for e in events]                                         

