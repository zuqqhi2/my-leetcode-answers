class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 212 ms, faster than 99.84%
#   Memory Usage: 15.3 MB, less than 27.56%
