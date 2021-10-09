class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return str(n)

        res = []
        cnt_from_last_dot = 0
        while n > 0:
            res.insert(0, str(n % 10))
            cnt_from_last_dot += 1
            if cnt_from_last_dot >= 3:
                res.insert(0, '.')
                cnt_from_last_dot = 0
            n = n // 10

        if res[0] == '.':
            del res[0]

        return ''.join(res)


# Performance Result:
#   Coding Time: 00:05:03
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 62.61%
#   Memory Usage: 14.3 MB, less than 44.44%
