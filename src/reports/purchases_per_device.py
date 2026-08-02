from collections import Counter

def purchases_per_device(events):
    purchases = []
    for event in events:
        purchases.append(event.device)
    purchases_cnt = Counter(purchases)
    return purchases_cnt