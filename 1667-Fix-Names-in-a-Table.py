import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')


# Performance Result:
#   Coding Time: 00:02:07
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 621 ms, faster than 26.48%
#   Memory Usage: 65.10 MB, less than 19.37%
