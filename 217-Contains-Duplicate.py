from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums) -> bool:
        # Corner cases
        if nums is None:
            return False
        if len(nums) == 0:
            return False

        num_counts = defaultdict(int)
        for value in nums:
            num_counts[value] += 1
            if num_counts[value] >= 2:
                return True

        return False


# Sample test case:
#   Input:
#       [1, 2, 3, 1]
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:03:01
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 136 ms, faster than 25.95% of Python3
#       online submissions for Contains Duplicate.
#   Memory Usage: 19 MB, less than 33.96% of Python3
#       online submissions for Contains Duplicate.
