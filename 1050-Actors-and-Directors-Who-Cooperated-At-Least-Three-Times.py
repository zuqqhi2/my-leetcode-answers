import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    res = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    return res[res['timestamp'] >= 3][['actor_id', 'director_id']]


# Performance Result:
#   Coding Time: 00:02:26
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 561 ms, faster than 77.95%
#   Memory Usage: 66.80 MB, less than 34.54%
