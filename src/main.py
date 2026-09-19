from ingestion.load_events import load_events
from reports.events_per_country import events_per_country
from reports.purchases_per_device import purchases_per_device
from reports.revenue_per_country import revenue_per_country
from reports.unique_users import unique_users
from reports.sort_events_by_revenue import sort_events_by_revenue
from reports.group_by_event_type import group_by_event_type
from processing.clean_events import clean_events
from processing.validate_events import validate_events
from processing.enrich_events import enrich_events
from processing.Pipeline import Pipeline

events = load_events("../data/events.csv")


my_pipeline = Pipeline(clean_events)
my_pipeline.add_step(validate_events)
my_pipeline.add_step(enrich_events)

enriched_events = my_pipeline(events)

print(len(enriched_events))
print(enriched_events)

