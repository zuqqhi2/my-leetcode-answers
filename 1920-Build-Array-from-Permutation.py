class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])

        return res


# Performance Result:
#   Coding Time: 00:02:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 128 ms, faster than 46.74%
#   Memory Usage: 14.4 MB, less than 71.52%
