import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    candidates = employee.groupby('managerId')['department'].count().reset_index()
    candidates = candidates[candidates['department'] >= 5][['managerId']]

    return employee[employee['id'].isin(candidates['managerId'])][['name']]


# Performance
#   Coding Time: 00:04:14
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 655 ms, faster than 50.30%
#   Memory Usage: 67.25 MB, less than 72.92%
