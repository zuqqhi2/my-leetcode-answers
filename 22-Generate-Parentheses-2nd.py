class Solution:
    def generate(self, n: int, m: int, cur_res: str = "") -> List[str]:
        """
        n: remaining start parenthes number
        m: remaining close parenthes number
        """
        if n == 0 and m == 0:
            return [cur_res]

        if n == 0 and m > 0:
            for i in range(m):
                cur_res += ")"
            return [cur_res]

        if n > 0 and m == 0:
            return []

        # open
        result = []
        result.extend(self.generate(n - 1, m, cur_res + "("))
        # close
        if n < m:
            result.extend(self.generate(n, m - 1, cur_res + ")"))

        return [e for e in result if len(e) > 0]

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n, n)


# Performance Result:
#   Coding Time: 00:08:25
#   Time Complexity: O(2^N)
#   Space Complexity: O(2^N)
#   Runtime: 32 ms, faster than 72.95%
#   Memory Usage: 13.9 MB, less than 6.67%
