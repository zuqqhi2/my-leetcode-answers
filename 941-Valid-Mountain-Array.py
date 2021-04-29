class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        is_increasing = True
        prev = arr[0]
        for i in range(1, len(arr)):
            if is_increasing:
                if arr[i] - prev == 0:
                    return False
                elif i == 1 and arr[i] - prev < 0:
                    return False
                elif arr[i] - prev < 0:
                    is_increasing = False
            else:
                if arr[i] - prev >= 0:
                    return False

            prev = arr[i]

        if is_increasing:
            return False

        return True


# Performance Result:
#   Coding Time: 00:06:29
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 196 ms, faster than 83.30%
#   Memory Usage: 15.6 MB, less than 9.74%
