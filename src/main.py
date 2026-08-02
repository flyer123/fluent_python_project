from ingestion.load_events import load_events
from processing.events_per_country import events_per_country
from processing.purchases_per_device import purchases_per_device
from processing.revenue_per_country import revenue_per_country
from processing.unique_users import unique_users
from processing.sort_events_by_revenue import sort_events_by_revenue
from processing.group_by_event_type import group_by_event_type

events = load_events("../data/events.csv")

print(len(events))

print(events[:3])

print(events_per_country(events))
print(purchases_per_device(events))
print(revenue_per_country(events))
print(unique_users(events))
print(sort_events_by_revenue(events))
print(group_by_event_type(events))