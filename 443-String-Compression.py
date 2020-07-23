class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        cnt = 0
        chars.append("dummy")
        for i in range(len(chars)):
            if i > 0 and chars[i - 1] != chars[i]:
                res.append(chars[i - 1])
                if cnt <= 1:
                    continue

                num = []
                while cnt > 0:
                    num.append(str(cnt % 10))
                    cnt //= 10
                res.extend(list(reversed(num)))
                cnt = 1
            else:
                cnt += 1

        chars[:] = res[:]
        return len(chars)


# Performance Result:
#   Coding Time: 00:26:06
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 72.62%
#   Memory Usage: 13.8 MB, less than 77.89%
