import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employees, employee_uni, how='left', on='id')
    return res[['unique_id', 'name']]


# Performance
#   Coding Time: 00:02:05
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 749 ms, faster than 36.95%
#   Memory Usage: 67.16 MB, less than 23.04%
