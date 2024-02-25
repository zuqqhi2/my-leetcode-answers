import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date': 'first_login'})


# Performance Result:
#   Coding Time: 00:02:41
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 614 ms, faster than 55.02%
#   Memory Usage: 66.79 MB, less than 56.02%
