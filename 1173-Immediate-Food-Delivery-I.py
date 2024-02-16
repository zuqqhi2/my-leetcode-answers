import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    numImmediate = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]['delivery_id'].count()
    res = round(numImmediate / float(delivery['delivery_id'].count()) * 100, 2)
    return pd.DataFrame(data=[res], columns=['immediate_percentage'])


# Performance Result:
#   Coding Time: 00:06:37
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 549 ms, faster than 71.94%
#   Memory Usage: 67.12 MB, less than 6.46%
