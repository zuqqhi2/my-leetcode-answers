import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['spent_time'] = employees['out_time'] - employees['in_time']
    res = employees.groupby(['emp_id', 'event_day'])['spent_time'].sum().reset_index()
    return res.rename(columns={'event_day': 'day', 'spent_time': 'total_time'})


# Performance Result:
#   Coding Time: 00:05:46
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 583 ms, faster than 86.57%
#   Memory Usage: 67.51 MB, less than 15.18%
