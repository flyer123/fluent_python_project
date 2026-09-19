import csv
import sys
from models.Event import Event
from datetime import datetime, date
import re
from typing import Any


pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
dateformat = "%Y-%m-%dT%H:%M:%S"

def check_convert(field: Any, type_to_check: type) -> bool:
    """Check whether object might be converted to a specific type.

    Args:
        field (Any): value to check
        type_to_check (type): type to try to convert to

    Return:
        True - if the object might be converted
        False - otherwise
    """
    try:
        type_to_check(field)
    except:
        return False
    return True

def convert_timestamp(pattern: str, timestamp: str) -> datetime:
    """Check whether timestamp string is in appropriate format.
    If so - return datetime created from it, otherwise - 
    return default value for 1970-01-01
    Args:

        pattern (str): pattern to check against
        timestamp (str): string value of the timestamp
            
    Return:
         datetime.timestamp
    """
        
                        
                    
    pattern = pattern
    timestamp = timestamp
    if re.fullmatch(pattern, timestamp):
        return datetime.strptime(timestamp, dateformat)
    else:
        return datetime.strptime('1970-01-01T:01:01:01', dateformat)          
                 


def load_events(path: str) -> list[Event]:
    """
    Read list of Event from a specified file

    Args:
        path (str): path to the spicefied file

    Return:
        list of Event
    """
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
                revenue=float(row["revenue"]),
                timestamp=convert_timestamp(pattern, row["timestamp"])
                ) 
            for row in reader if check_convert(row["event_id"], int) and check_convert(row["revenue"], float)
        ]
    return events

