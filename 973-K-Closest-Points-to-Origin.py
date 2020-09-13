import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            dist = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            heapq.heappush(heap, [-dist, points[i]])
            if len(heap) > K:
                heapq.heappop(heap)

        return [e[1] for e in heap]


# Performance Result:
#   Coding Time: 00:05:40
#   Time Complexity: O(N log N)
#   Space Complexity: O(K)
#   Runtime: 1048 ms, faster than 17.62%
#   Memory Usage: 19 MB, less than 88.76%
