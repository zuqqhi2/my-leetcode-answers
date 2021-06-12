class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str,
                     ruleValue: str) -> int:
        key_idx = {'type': 0, 'color': 1, 'name': 2}

        res = 0
        for item in items:
            if item[key_idx[ruleKey]] == ruleValue:
                res += 1

        return res


# Performance Result:
#   Coding Time: 00:02:07
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 248 ms, faster than 41.04%
#   Memory Usage: 20.4 MB, less than 86.89%
