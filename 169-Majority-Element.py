import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        max_freq_num = nums[0]
        max_freq = 1
        for num in counts.keys():
            if counts[num] > max_freq:
                max_freq_num = num
                max_freq = counts[num]

        return max_freq_num


# Performance Result:
#   Coding Time: 00:04:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 176 ms, faster than 61.09%
#   Memory Usage: 15.3 MB, less than 21.39%
