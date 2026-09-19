from collections import Counter
from models.Event import Event

def purchases_per_device(events: list[Event]) -> Counter[str]:
    purchases = []
    for event in events:
        purchases.append(event.device)
    purchases_cnt = Counter(purchases)
    return purchases_cnt