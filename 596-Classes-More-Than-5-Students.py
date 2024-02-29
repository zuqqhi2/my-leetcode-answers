import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class')['student'].count().reset_index()
    return res[res['student'] >= 5][['class']]


# Performance Result:
#   Coding Time: 00:01:53
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 786 ms, faster than 5.04%
#   Memory Usage: 67.16 MB, less than 18.14%
