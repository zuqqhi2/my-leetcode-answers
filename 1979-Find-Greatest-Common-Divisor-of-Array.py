class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return math.gcd(smallest, largest)

# Performance Result:
#   Coding Time: 00:03:10
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 54 ms, faster than 86.76%
#   Memory Usage: 14.0 MB, less than 70.55%
