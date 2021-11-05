class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high = high + 1 - low if low % 2 == 1 else high - low
        return high // 2 + 1 if high % 2 == 1 else high // 2


# Performance Result:
#   Coding Time: 00:19:00
#   Time Complexity: O(1)
#   Space Complexity: O(1)
#   Runtime: 24 ms, faster than 93.06%
#   Memory Usage: 14.3 MB, less than 9.95%
