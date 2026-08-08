from datetime import datetime, date
from dataclasses import dataclass
from models.Event import Event

dateformat = "%Y-%m-%dT%H:%M:%S"


@dataclass(frozen=True)
class EnrichedEvent(Event):
    is_purchase: bool
    revenue_band: str
    timestamp: datetime
    weekday: str

    @classmethod
    def from_event(cls, event: Event):

        # exclude key handled in EnrichedEvent
        exclude_keys = {"timestamp"}

        filtered_dict = {
            k: v for k, v in event.__dict__.items()
            if k not in exclude_keys
        }

        is_purchase = event.event_type == "purchase"
        if event.revenue <= 75:
            revenue_band = "low"
        elif event.revenue <= 150:
            revenue_band = "medium"
        else:
            revenue_band = "high"
        return cls(
            **filtered_dict,
            is_purchase = is_purchase,
            revenue_band = revenue_band,
            timestamp = datetime.strptime(event.timestamp, dateformat),
            weekday = datetime.strptime(event.timestamp, dateformat).strftime("%A")
        )