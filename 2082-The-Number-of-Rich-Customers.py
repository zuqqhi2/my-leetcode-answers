import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    customersMaxAmount = store.groupby('customer_id')['amount'].max()
    countRes = (customersMaxAmount > 500).sum()
    return pd.DataFrame(data=[countRes], columns=['rich_count'])


# Performance Result:
#   Coding Time: 00:10:23
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 584 ms, faster than 36.45%
#   Memory Usage: 66.67 MB, less than 6.67%
