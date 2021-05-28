class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr[:] = sorted(arr)

        num_apples = 0
        sum_weight = 0
        for i in range(len(arr)):
            sum_weight += arr[i]
            if sum_weight > 5000:
                break
            num_apples += 1

        return num_apples


# Performance Result:
#   Coding Time: 00:03:04
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 92.04%
#   Memory Usage: 14.1 MB, less than 94.69%
