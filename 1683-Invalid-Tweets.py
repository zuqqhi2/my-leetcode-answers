import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]


# Performance Result:
#   Coding Time: 00:05:13
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 725 ms, faster than 5.02%
#   Memory Usage: 65.55 MB, less than 13.25%
