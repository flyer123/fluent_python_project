from dataclasses import dataclass
from datetime import datetime, date

@dataclass(frozen=True)
class Event:
    event_id: int
    user_id: str
    event_type: str
    source: str
    country: str
    device: str
    revenue: float
    timestamp: datetime
