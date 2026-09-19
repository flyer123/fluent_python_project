from collections import Counter
from models.Event import Event

def events_per_country(events: list[Event]) -> Counter[str]:
    countries = []
    for event in events:
        countries.append(event.country)
    countries_cnt = Counter(countries)
    return countries_cnt