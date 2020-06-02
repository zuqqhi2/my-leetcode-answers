import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum_map = collections.defaultdict(int)
        cum_sum_map[0] = 1
        num_arr = 0
        total = 0
        for i, v in enumerate(nums):
            total += v
            if total - k in cum_sum_map:
                num_arr += cum_sum_map[total - k]
            cum_sum_map[total] += 1

        return num_arr


# Performance Result:
#   Coding Time: 00:06:40
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 144 ms, faster than 19.66%
#   Memory Usage: 16.2 MB, less than 20.00%
