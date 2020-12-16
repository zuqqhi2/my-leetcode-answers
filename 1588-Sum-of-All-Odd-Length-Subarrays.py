class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for step in range(1, len(arr) + 1, 2):
            sub_sum = 0
            for i in range(len(arr) - step + 1):
                for j in range(i, i + step):
                    sub_sum += arr[j]

            res += sub_sum

        return res


# Performance Result:
#   Coding Time: 00:18:49
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 140 ms, faster than 14.08%
#   Memory Usage: 13.9 MB, less than 99.96%
