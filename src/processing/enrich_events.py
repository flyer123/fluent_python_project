from models.Event import Event
from models.EnrichedEvent import EnrichedEvent


def enrich_events(events):
    return [EnrichedEvent.from_event(e) for e in events]                                         

