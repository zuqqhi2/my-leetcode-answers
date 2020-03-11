class Solution:
    def productExceptSelf(self, nums):
        # Corner cases
        if nums is None:
            return []
        if len(nums) == 0:
            return []

        length = len(nums)
        results = [0] * length
        # Left to right
        results[0] = 1
        for i in range(1, length):
            results[i] = nums[i - 1] * results[i - 1]

        # Right to left
        tmp_product = 1
        for i in reversed(range(length)):
            results[i] = results[i] * tmp_product
            tmp_product *= nums[i]

        return results


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))


# Sample test case:
#   Input:
#       [1, 2, 3, 1]
#   Output:
#       True

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 120 ms, faster than 87.74% of Python3
#       online submissions for Product of Array Except Self.
#   Memory Usage: 19.4 MB, less than 96.00% of Python3
#       online submissions for Product of Array Except Self.
