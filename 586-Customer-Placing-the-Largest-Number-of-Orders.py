import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    res = orders.groupby('customer_number')['order_number'].count().reset_index()
    return res.nlargest(1, 'order_number')[['customer_number']]


# Performance Result:
#   Coding Time: 00:09:21
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 656 ms, faster than 29.24%
#   Memory Usage: 66.31 MB, less than 23.49%
