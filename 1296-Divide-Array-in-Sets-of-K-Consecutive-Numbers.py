import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        for num in sorted(c):
            if c[num] > 0:
                for i in range(k)[::-1]:
                    c[num + i] -= c[num]
                    if c[num + i] < 0:
                        return False

        return True


# Performance Result:
#   Coding Time: 00:18:19
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 452 ms, faster than 77.98%
#   Memory Usage: 29.4 MB, less than 23.21%
