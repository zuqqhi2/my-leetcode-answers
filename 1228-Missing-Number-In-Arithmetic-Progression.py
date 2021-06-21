class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diffs = [0, 0]
        diff_count = [0, 0]
        for i in range(len(arr) - 1):
            if diffs[0] == 0:
                diffs[0] = arr[i + 1] - arr[i]
                diff_count[0] += 1
            elif diffs[0] == arr[i + 1] - arr[i]:
                diff_count[0] += 1
            elif diffs[1] == 0:
                diffs[1] = arr[i + 1] - arr[i]
                diff_count[1] += 1
            else:
                diff_count[1] += 1

        target_diff = 0
        if diff_count[0] == diff_count[1]:
            if diffs[0] >= 0 and diffs[1] >= 0:
                target_diff = max(diffs[0], diffs[1])
            else:
                target_diff = min(diffs[0], diffs[1])
        else:
            if diff_count[0] > diff_count[1]:
                target_diff = diffs[1]
            else:
                target_diff = diffs[0]

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == target_diff:
                if diffs[0] == target_diff:
                    return arr[i] + diffs[1]
                else:
                    return arr[i] + diffs[0]

        return 0


# Performance Result:
#   Coding Time: 00:23:07
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 48 ms, faster than 32.69%
#   Memory Usage: 14.5 MB, less than 6.07%
