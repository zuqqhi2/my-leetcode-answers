class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        diff_nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        diff_nums = list(filter(lambda x: x != 0, diff_nums))
        # [2, -3, 0, 5, -1]

        num_hill_or_valley = 0
        for i in range(len(diff_nums) - 1):
            # hill
            if diff_nums[i] > 0 and diff_nums[i + 1] < 0:
                num_hill_or_valley += 1
            # valley
            elif diff_nums[i] < 0 and diff_nums[i + 1] > 0:
                num_hill_or_valley += 1

        return num_hill_or_valley

# Performance Result:
#   Coding Time: 00:10:53
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 33 ms, faster than 94.00%
#   Memory Usage: 13.9 MB, less than 58.75%
