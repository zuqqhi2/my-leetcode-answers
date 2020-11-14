class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return True

        arr[:] = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True


# Performance Result:
#   Coding Time: 00:02:38
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 61.76%
#   Memory Usage: 14.3 MB, less than 18.42%
