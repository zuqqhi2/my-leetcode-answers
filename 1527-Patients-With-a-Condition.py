import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains('(^DIAB1)|( DIAB1)')]


# Performance Result:
#   Coding Time: 00:01:55
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 479 ms, faster than 66.20%
#   Memory Usage: 65.38 MB, less than 15.76%
