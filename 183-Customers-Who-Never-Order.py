import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_order = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    return cust_order[cust_order['customerId'].isnull()][['name']].rename(columns={'name': 'Customers'})


# Performance Result:
#   Coding Time: 00:10:45
#   Time Complexity: O(N)
#   Space Complexity: O(n)
#   Runtime: 504 ms, faster than 58.75%
#   Memory Usage: 61.45 MB, less than 36.08%
