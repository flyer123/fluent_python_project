from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    event_id: int
    user_id: str
    event_type: str
    source: str
    country: str
    device: str
    revenue: float
    timestamp: str
