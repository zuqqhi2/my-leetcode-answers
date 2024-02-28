import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[['teacher_id', 'subject_id']].drop_duplicates().groupby(
        'teacher_id')['subject_id'].count().reset_index().rename(
        columns={'subject_id': 'cnt'})


# Performance Result:
#   Coding Time: 00:06:13
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 657 ms, faster than 30.27%
#   Memory Usage: 66.88 MB, less than 39.56%
