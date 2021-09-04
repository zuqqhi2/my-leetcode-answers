class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


# Performance Result:
#   Coding Time: 00:01:54
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 84 ms, faster than 74.86%
#   Memory Usage: 14.7 MB, less than 21.59%
