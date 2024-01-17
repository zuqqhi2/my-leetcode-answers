import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id'] == views['viewer_id']][['author_id']] \
        .rename(columns={'author_id': 'id'}) \
        .drop_duplicates() \
        .sort_values('id')


# Performance Result:
#   Coding Time: 00:07:53
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 632 ms, faster than 14.73%
#   Memory Usage: 60.56 MB, less than 93.78%
