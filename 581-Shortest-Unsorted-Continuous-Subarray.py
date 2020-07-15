class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        start = 0
        while start < len(nums) and nums[start] == sorted_nums[start]:
            start += 1

        end = len(nums) - 1
        while end >= 0 and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1 if end > start else 0


# Performance Result:
#   Coding Time: 00:06:47
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 212 ms, faster than 83.47%
#   Memory Usage: 15.1 MB, less than 22.00%
