class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_valley_idx = len(nums) - 2
        while last_valley_idx >= 0 and nums[last_valley_idx] >= nums[
            last_valley_idx + 1]:
            last_valley_idx -= 1

        if last_valley_idx < 0:
            nums[:] = reversed(nums[:])
        else:
            last_bigger_idx = len(nums) - 1
            while last_bigger_idx > last_valley_idx and nums[last_bigger_idx] <= \
                nums[last_valley_idx]:
                last_bigger_idx -= 1

            nums[last_valley_idx], nums[last_bigger_idx] = nums[
                                                               last_bigger_idx], \
                                                           nums[last_valley_idx]

            nums[last_valley_idx + 1:] = reversed(nums[last_valley_idx + 1:])


# Performance Result:
#   Coding Time: 00:14:15
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 90.68%
#   Memory Usage: 13.9 MB, less than 5.56%
