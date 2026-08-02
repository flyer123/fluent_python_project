from collections import Counter

def events_per_country(events):
    countries = []
    for event in events:
        countries.append(event.country)
    countries_cnt = Counter(countries)
    return countries_cnt