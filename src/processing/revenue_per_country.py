from collections import defaultdict

def revenue_per_country(rows):
    revenue_dict = defaultdict(list)
    for row in rows:
        revenue_dict[row[5]] += row[7]
    return revenue_dict



















