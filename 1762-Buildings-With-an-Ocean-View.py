class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_heights = [0] * len(heights)
        for i in reversed(range(1, len(heights))):
            if i == len(heights) - 1:
                max_heights[i] = heights[i]
            else:
                max_heights[i] = max(heights[i], max_heights[i + 1])

        res = []
        for i in range(len(heights) - 1):
            if heights[i] > max_heights[i + 1]:
                res.append(i)

        res.append(len(heights) - 1)
        return res


# Performance Result:
#   Coding Time: 00:13:00
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 836 ms, faster than 15.20%
#   Memory Usage: 31.8 MB, less than 31.13%
