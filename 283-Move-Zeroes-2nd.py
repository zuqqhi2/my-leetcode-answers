class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2-Pointers
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            if nums[left_idx] != 0:
                left_idx += 1
                continue

            nums.append(0)
            del nums[left_idx]
            right_idx -= 1


# Performance Result:
#   Coding Time: 00:05:48
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 44.81% of Python3
#       online submissions for Move Zeroes.
#   Memory Usage: 14 MB, less than 100.00% of Python3
#       online submissions for Move Zeroes.
