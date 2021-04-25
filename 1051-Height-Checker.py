class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_heights = sorted(heights)

        num_diff = 0
        for i in range(len(heights)):
            num_diff += 1 if heights[i] != expected_heights[i] else 0

        return num_diff


# Performance Result:
#   Coding Time: 00:02:19
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 83.81%
#   Memory Usage: 14.3 MB, less than 44.07%
