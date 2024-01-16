import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return products[['product_id']]


# Performance Result:
#   Coding Time: 00:01:35
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 577 ms, faster than 34.74%
#   Memory Usage: 61.18 MB, less than 49.50%
