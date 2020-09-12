class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])

        return res


# Performance Result:
#   Coding Time: 00:02:28
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 63.72%
#   Memory Usage: 13.9 MB, less than 85.15%
