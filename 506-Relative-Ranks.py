import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [-score[i] for i in range(len(score))]
        heapq.heapify(heap)
        rank = {}
        for i in range(len(score)):
            value = heapq.heappop(heap)
            if i + 1 == 1:
                rank[-value] = 'Gold Medal'
            elif i + 1 == 2:
                rank[-value] = 'Silver Medal'
            elif i + 1 == 3:
                rank[-value] = 'Bronze Medal'
            else:
                rank[-value] = str(i + 1)

        res = []
        for i in range(len(score)):
            res.append(rank[score[i]])

        return res


# Performance Result:
#   Coding Time: 00:06:21
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 68 ms, faster than 85.81%
#   Memory Usage: 15.6 MB, less than 10.90%
