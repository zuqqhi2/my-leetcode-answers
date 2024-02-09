import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores.drop(columns='id').sort_values('score', ascending=False)


# Performance Result:
#   Coding Time: 00:02:22
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 738 ms, faster than 5.06%
#   Memory Usage: 66.68 MB, less than 25.34%
