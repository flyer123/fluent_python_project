import csv
import sys
from models.Event import Event

def load_events(path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        events = [ 
            Event(
                event_id=int(row["event_id"]),
                user_id=row["user_id"],
                event_type=row["event_type"],
                source=row["source"],
                country=row["country"],
                device=row["device"],
                revenue=int(row["revenue"]),
                timestamp=row["timestamp"]
                )
            for row in reader
        ]
    return events

