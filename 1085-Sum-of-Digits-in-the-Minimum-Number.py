class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        while min_num > 0:
            res += min_num % 10
            min_num = int(min_num / 10)
        if res % 2 == 0:
            return 1
        else:
            return 0


# Performance Result:
#   Coding Time: 00:05:11
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 0 ms, faster than 100.00%
#   Memory Usage: 17.96 MB, less than 23.21%