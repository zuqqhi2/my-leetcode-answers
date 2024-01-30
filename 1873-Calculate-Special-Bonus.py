import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']
    employees['bonus'] = employees.where((employees['employee_id'] % 2 == 1) & ~(employees['name'].str.startswith('M')), 0)['bonus']
    return employees[['employee_id', 'bonus']].sort_values('employee_id')


# Performance Result:
#   Coding Time: 00:17:28
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 713 ms, faster than 14.77%
#   Memory Usage: 67.23 MB, less than 6.70%
