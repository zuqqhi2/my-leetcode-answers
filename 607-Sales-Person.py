import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(sales_person, orders, on='sales_id', how='left')
    res = pd.merge(res, company, on='com_id', how='left')
    res = res.groupby(['sales_id', 'name_x'])['name_y'].apply(list).reset_index()
    mask = res['name_y'].apply(lambda x: 'RED' not in x)
    res = res[mask].rename(columns={'name_x': 'name'})[['name']]

    return res


# Performance
#   Coding Time: 00:11:24
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 942 ms, faster than 29.40%
#   Memory Usage: 67.38 MB, less than 59.63%
