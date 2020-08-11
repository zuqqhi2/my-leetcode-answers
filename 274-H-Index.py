class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0

        citations = list(sorted(citations, key=lambda x: -x))
        max_h = 0
        for i in range(len(citations) - 1):
            h = i + 1
            if citations[i] >= h and citations[i + 1] <= h:
                max_h = h

        last_idx = len(citations) - 1
        if citations[last_idx] >= last_idx + 1:
            max_h = last_idx + 1

        return max_h


# Performance Result:
#   Coding Time: 00:15:19
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 53.13%
#   Memory Usage: 14 MB, less than 66.18%
