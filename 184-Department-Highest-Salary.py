import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employee, department, left_on='departmentId', right_on='id').drop(columns=['id_x', 'departmentId', 'id_y'])
    res = res.rename(columns={
        'name_x': 'Employee',
        'salary': 'Salary',
        'name_y': 'Department'})
    res['grank'] = res.groupby('Department')['Salary'].rank(method='dense', ascending=False)
    return res[res['grank'] == 1].drop(columns='grank')


# Performance Result:
#   Coding Time: 00:14:29
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 624 ms, faster than 60.78%
#   Memory Usage: 67.63 MB, less than 16.74%
