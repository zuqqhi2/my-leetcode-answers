import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users = users[(users['mail'].str.contains('^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'))]
    return users


# Performance Result:
#   Coding Time: 00:04:32
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 747 ms, faster than 5.65%
#   Memory Usage: 66.74 MB, less than 6.36%
