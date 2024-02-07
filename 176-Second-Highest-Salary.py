import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates('salary', keep='last')
    employee = employee.sort_values('salary', ascending=False)
    if len(employee['salary']) >= 2:
        return pd.DataFrame({'SecondHighestSalary': [employee['salary'].iloc[1]]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})


# Performance Result:
#   Coding Time: 00:05:51
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 497 ms, faster than 54.59%
#   Memory Usage: 65.45 MB, less than 23.91%
