class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums is None:
            return None
        if len(nums) <= 1:
            return None

        # Swap small upper level digit and big lower level digit
        for i in reversed(range(len(nums) - 1)):
            min_val = 1e+6
            min_idx = -1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and min_val > nums[j]:
                    min_val = nums[j]
                    min_idx = j

            if min_idx > -1:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return None

        # if there was no swap, find minimum number
        nums.sort()
        return None


s = Solution()

in_list = [1, 3, 2]
s.nextPermutation(in_list)
print(in_list)

in_list = [5, 4, 7, 5, 3, 2]
s.nextPermutation(in_list)
print(in_list)

in_list = [4, 2, 0, 2, 3, 2, 0]
s.nextPermutation(in_list)
print(in_list)

# Sample test case:
#   Input:
#       [1, 3, 2]
#   Output:
#       [2, 1, 3]

# Performance Result:
#   Coding Time: 00:38:27
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 68.35% of Python3
#       online submissions for Next Permutation.
#   Memory Usage: 12.8 MB, less than 100.00% of Python3
#       online submissions for Next Permutation.
