from collections import Counter

def events_per_country(rows):
    countries = []
    for row in rows:
        countries.append(row[5])
    countries_cnt = Counter(countries)
    return countries_cnt