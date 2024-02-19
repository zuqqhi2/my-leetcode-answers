import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts['income'] < 20000]['income'].count()
    ave_salary = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]['income'].count()
    high_salary = accounts[accounts['income'] > 50000]['income'].count()
    print([low_salary, ave_salary, high_salary])

    return pd.DataFrame(data=[
        ['Low Salary', low_salary],
        ['Average Salary', ave_salary],
        ['High Salary', high_salary]],
        columns=['category', 'accounts_count'])


# Performance Result:
#   Coding Time: 00:07:43
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 622 ms, faster than 71.97%
#   Memory Usage: 89.36 MB, less than 23.51%
