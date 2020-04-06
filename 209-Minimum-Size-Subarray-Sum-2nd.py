class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        min_length = 1_000_000
        for right in range(len(nums)):
            cur_sum += nums[right]
            if cur_sum < s:
                continue

            min_length = min(min_length, right - left + 1)
            while cur_sum >= s and left <= right:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return min_length if min_length < 1_000_000 else 0


# Performance Result:
#   Coding Time: 00:10:40
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 76 ms, faster than 67.24% of Python3
#       online submissions for Minimum Size Subarray Sum.
#   Memory Usage: 16.4 MB, less than 7.69% of Python3
#       online submissions for Minimum Size Subarray Sum.
