from collections import OrderedDict

def top_revenue_by_country(revenue_dict):
    return OrderedDict(sorted(revenue_dict.items(), key=lambda item: item[1]))