import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna(subset='price')


# Performance Result:
#   Coding Time: 00:21:27
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 619 ms, faster than 63.47%
#   Memory Usage: 66.34 MB, less than 21.70%
