import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return world[['name', 'population', 'area']]


# Performance Result:
#   Coding Time: 00:04:44
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 502 ms, faster than 44.43%
#   Memory Usage: 62.79 MB, less than 47.50%
