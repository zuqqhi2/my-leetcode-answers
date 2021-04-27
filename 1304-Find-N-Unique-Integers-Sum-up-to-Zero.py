class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:
            res.append(0)
            n -= 1

        cur_num = 1
        while n > 0:
            res.append(cur_num)
            res.append(-cur_num)
            cur_num += 1
            n -= 2

        return res


# Performance Result:
#   Coding Time: 00:03:17
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 47.02%
#   Memory Usage: 14.5 MB, less than 19.53%
