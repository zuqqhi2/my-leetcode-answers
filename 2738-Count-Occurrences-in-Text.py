import pandas as pd


def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull_count = files['content'].str.contains(' bull ').sum()
    bear_count = files['content'].str.contains(' bear ').sum()

    return pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]
    })


# Performance Result:
#   Coding Time: 00:08:23
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 511 ms, faster than 51.45%
#   Memory Usage: 65.21 MB, less than 17.60%
