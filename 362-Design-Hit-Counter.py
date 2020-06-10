import collections


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = collections.defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.history[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        num_hits = 0
        first_ts = max(0, timestamp - 299)
        for key in self.history.keys():
            num_hits += self.history[key] if first_ts <= key <= timestamp else 0

        return num_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Performance Result:
#   Coding Time: 00:17:33
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 79.71%
#   Memory Usage: 13.8 MB, less than 58.89%
