class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_dec += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count_dec > 1:
                return False
        return True


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 240 ms, faster than 30.48%
#   Memory Usage: 14.9 MB, less than 74.47%
