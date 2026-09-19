from collections import OrderedDict
from collections import defaultdict

def top_revenue_by_country(revenue_dict: defaultdict[str, float]) -> OrderedDict[str, float]:
    return OrderedDict(sorted(revenue_dict.items(), key=lambda item: item[1]))