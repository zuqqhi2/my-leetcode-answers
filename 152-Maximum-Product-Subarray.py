class Solution:
    def maxProduct(self, nums) -> int:
        # Corner cases
        if nums is None:
            return 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        res = cmin = cmax = nums[0]
        for n in nums[1:]:
            cmin, cmax = min(n, cmin * n, cmax * n), max(n, cmin * n, cmax * n)
            if cmax > res: res = cmax
        return res


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))

# Sample test case:
#   Input:
#       [2, 3, -2, 4]
#   Output:
#       6

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 56 ms, faster than 62.02% of Python3
#       online submissions for Maximum Product Subarray.
#   Memory Usage: 13 MB, less than 100.00% of Python3
#       online submissions for Maximum Product Subarray.
