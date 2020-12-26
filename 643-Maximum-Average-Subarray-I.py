class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val = sum(nums[0:k])
        cur_val = sum(nums[0:k])
        for i in range(k, len(nums)):
            cur_val += nums[i] - nums[i - k]
            max_val = max(max_val, cur_val)

        return max_val / float(k)


# Performance Result:
#   Coding Time: 00:08:43
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 836 ms, faster than 54.84%
#   Memory Usage: 18.1 MB, less than 36.54%
