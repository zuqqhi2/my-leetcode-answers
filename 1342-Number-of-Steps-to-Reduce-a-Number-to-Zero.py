class Solution:
    def numberOfSteps(self, num: int) -> int:
        num_step = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            num_step += 1

        return num_step


# Performance Result:
#   Coding Time: 00:01:37
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 78.82%
#   Memory Usage: 14 MB, less than 99.98%
