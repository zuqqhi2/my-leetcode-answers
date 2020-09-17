class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        average, remainder, part, cnt = sum(A) // 3, sum(A) % 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return not remainder and cnt >= 3


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 324 ms, faster than 89.02%
#   Memory Usage: 20.3 MB, less than 90.58%
