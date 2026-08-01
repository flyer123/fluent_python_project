from collections import Counter

def purchases_per_device(rows):
    purchases = []
    for row in rows:
        purchases.append(row[6])
    purchases_cnt = Counter(purchases)
    return purchases_cnt