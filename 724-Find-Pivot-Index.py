class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num_len = len(nums)

        if num_len == 0:
            return -1
        if num_len == 1:
            return nums[0]

        left_acc = [nums[0]]
        for i in range(1, num_len):
            left_acc.append(left_acc[i - 1] + nums[i])

        for i in range(num_len):
            if i == 0 and left_acc[-1] - left_acc[i] == 0:
                return i
            elif i == num_len - 1 and left_acc[i - 1] == 0:
                return i
            elif 0 < i < num_len - 1 and left_acc[i - 1] == left_acc[-1] - \
                left_acc[i]:
                return i

        return - 1


# Performance Result:
#   Coding Time: 00:10:52
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 348 ms, faster than 14.19%
#   Memory Usage: 15.1 MB, less than 27.83%
