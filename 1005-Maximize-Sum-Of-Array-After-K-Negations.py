import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for i in range(K):
            min_val = heapq.heappop(A)
            heapq.heappush(A, -min_val)

        return sum(A)


# Performance Result:
#   Coding Time: 00:04:11
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 99.82%
#   Memory Usage: 14.4 MB, less than 38.38%
