# Algorithm: Sliding Window
# How to work:
#   left index: will be +1 sum(arr[left:right]) >= 7
#   right index: will be +1 while sum(arr[left:right]) < 7
class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0 and s > 0:
            return 0

        min_length = 1000000
        left = 0
        for right in range(1, len(nums) + 1):
            sum_val = sum(nums[left:right])
            if sum_val >= s:
                if min_length > right - left:
                    min_length = right - left

                while True:
                    left += 1
                    if left <= right - 1 and sum(nums[left:right]) >= s:
                        if min_length > right - left:
                            min_length = right - left
                    else:
                        break

        if min_length = 1000000:
            return 0
        else:
            return min_length


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(7, [7]))
print(s.minSubArrayLen(7, [2, 5]))
print(s.minSubArrayLen(7, []))
print(s.minSubArrayLen(7, [7]))
print(s.minSubArrayLen(80, [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]))
print(s.minSubArrayLen(4, [1, 4, 4]))

# Sample test case:
#   Input:
#       s = 7, nums = [2,3,1,2,4,3]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:23:06
#   Time Complexity: O(N) Note: 2N
#   Space Complexity: O(1)
#   Runtime: 2740 ms, faster than 5.11% of Python3
#       online submissions for Minimum Size Subarray Sum.
#   Memory Usage: 15.2 MB, less than 7.69% of Python3
#       online submissions for Minimum Size Subarray Sum.
