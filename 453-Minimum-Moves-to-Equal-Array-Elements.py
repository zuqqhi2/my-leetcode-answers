class Solution:
    def minMoves(self, nums: List[int]) -> int:
        num_attempt = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            num_attempt += nums[i] - nums[0]

        return num_attempt


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 356 ms, faster than 34.85%
#   Memory Usage: 15.1 MB, less than 82.61%
