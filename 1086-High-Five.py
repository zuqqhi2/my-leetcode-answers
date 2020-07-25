import heapq
import collections


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        top5_score = collections.defaultdict(list)
        for id, score in items:
            heapq.heappush(top5_score[id], score)
            if len(top5_score[id]) > 5:
                heapq.heappop(top5_score[id])

        res = []
        for key in top5_score.keys():
            res.append([key, int(sum(top5_score[key]) / len(top5_score[key]))])
        return res


# Performance Result:
#   Coding Time: 00:08:53
#   Time Complexity: O(N log N)
#   Space Complexity: O(M)
#   Runtime: 76 ms, faster than 78.88%
#   Memory Usage: 14.3 MB, less than 10.68%
