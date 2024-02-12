import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    person.drop_duplicates('email', keep='first', inplace=True)


# Performance Result:
#   Coding Time: 00:04:19
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 612 ms, faster than 25.17%
#   Memory Usage: 66.45 MB, less than 10.75%
