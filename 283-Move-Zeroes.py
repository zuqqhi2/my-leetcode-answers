class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return None
        elif len(nums) <= 1:
            return None

        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                nums.append(nums[idx])
                nums.pop(idx)

                finish_flg = True
                for j in range(idx, len(nums)):
                    if nums[j] != 0:
                        finish_flg = False
                        break
                if finish_flg:
                    return None
            else:
                idx += 1

        return None


# Sample test case:
#   Input:
#       [0,1,0,3,12]
#   Output:
#       [1,3,12,0,0]

# Performance Result:
#   Coding Time: 00:13:24
#   Time Complexity: O(n^2)
#   Space Complexity: O(n)
#   Runtime: 60 ms, faster than 65.28% of Python3
#       online submissions for Move Zeroes.
#   Memory Usage: 15.2 MB, less than 5.97% of Python3
#       online submissions for Move Zeroes.
