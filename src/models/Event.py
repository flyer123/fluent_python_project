from dataclasses import dataclasses

@dataclass
class Event(frozen=True):
    event_id: int
    user_id: str
    event_type: str
    source: str
    country: str
    device: str
    revenue: float
    timestamp: str
