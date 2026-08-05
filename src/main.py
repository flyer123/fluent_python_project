from ingestion.load_events import load_events
from reports.events_per_country import events_per_country
from reports.purchases_per_device import purchases_per_device
from reports.revenue_per_country import revenue_per_country
from reports.unique_users import unique_users
from reports.sort_events_by_revenue import sort_events_by_revenue
from reports.group_by_event_type import group_by_event_type
from processing.clean_events import clean_events

events = load_events("../data/events.csv")

print(len(events))

print(events[:3])

cleaned_events = clean_events(events)
print(len(cleaned_events))

print(cleaned_events[:3])
print(events_per_country(cleaned_events))
print(purchases_per_device(cleaned_events))
print(revenue_per_country(cleaned_events))
print(unique_users(cleaned_events))
print(sort_events_by_revenue(cleaned_events))
print(group_by_event_type(cleaned_events)) 