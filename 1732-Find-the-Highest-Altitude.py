class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        cur = 0
        for i in range(len(gain)):
            cur += gain[i]
            max_altitude = max(max_altitude, cur)

        return max_altitude


# Performance Result:
#   Coding Time: 00:02:34
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 70.49%
#   Memory Usage: 14.3 MB, less than 8.00%
