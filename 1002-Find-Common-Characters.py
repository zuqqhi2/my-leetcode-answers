import collections


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt = collections.Counter(A[0])
        for i in range(1, len(A)):
            tmp_cnt = collections.Counter(A[i])

            new_cnt = {}
            for k in cnt:
                if k in tmp_cnt:
                    new_cnt[k] = min(cnt[k], tmp_cnt[k])
            cnt = new_cnt

        res = []
        for k in cnt:
            for i in range(cnt[k]):
                res.append(k)

        return res


# Performance Result:
#   Coding Time: 00:05:50
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 56 ms, faster than 56.73%
#   Memory Usage: 13.8 MB, less than 79.75%
