class Solution:
    def isHappy(self, n: int) -> bool:
        sq_sum = 0
        num_attempts = 0
        cur_n = n
        while sq_sum != 1 and num_attempts <= 1000:
            sq_sum = 0
            while cur_n != 0:
                sq_sum += (cur_n % 10) ** 2
                cur_n = cur_n // 10

            num_attempts += 1
            cur_n = sq_sum

        return True if sq_sum == 1 else False


# Performance Result:
#   Coding Time: 00:06:38
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 364 ms, faster than 5.05%
#   Memory Usage: 13.8 MB, less than 45.51%
