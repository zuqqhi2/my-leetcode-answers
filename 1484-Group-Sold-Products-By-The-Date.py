import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    unique_activities = activities.drop_duplicates()
    cnts = unique_activities.groupby('sell_date')['product'].count().reset_index()
    products = unique_activities.groupby('sell_date')['product'].apply(list).apply(lambda x: sorted(x)).apply(','.join).reset_index()
    return pd.merge(cnts, products, on='sell_date').rename(columns={'product_x': 'num_sold', 'product_y': 'products'})


# Performance Result:
#   Coding Time: 00:09:14
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 685 ms, faster than 59.68%
#   Memory Usage: 67.89 MB, less than 21.91%
