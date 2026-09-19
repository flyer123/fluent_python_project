from dataclasses import dataclass
from models.Event import Event
from datetime import datetime, date



@dataclass(frozen=True)
class EnrichedEvent(Event):
    is_purchase: bool
    revenue_band: str
    weekday: str

    @classmethod
    def from_event(cls, event: Event):
        
        is_purchase = event.event_type == "purchase"
        if event.revenue <= 75:
            revenue_band = "low"
        elif event.revenue <= 150:
            revenue_band = "medium"
        else:
            revenue_band = "high"
        return cls(
            #**filtered_dict,
            **event.__dict__,
            is_purchase = is_purchase,
            revenue_band = revenue_band,
            weekday = event.timestamp.strftime("%A")
        )