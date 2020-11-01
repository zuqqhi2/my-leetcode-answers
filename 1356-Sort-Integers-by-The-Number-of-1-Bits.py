class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (format(x, 'b').count('1'), x))


# Performance Result:
#   Coding Time: 00:07:18
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 76 ms, faster than 45.71%
#   Memory Usage: 14.3 MB, less than 100.00%
