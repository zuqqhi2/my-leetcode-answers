import heapq


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []

        heap = []
        for v in arr:
            heapq.heappush(heap, v)

        cur_val = heapq.heappop(heap)
        rank = {cur_val: 1}
        prev = cur_val
        cur_rank = 2
        while len(heap) > 0:
            cur_val = heapq.heappop(heap)
            if cur_val == prev:
                continue

            rank[cur_val] = cur_rank
            prev = cur_val
            cur_rank += 1

        res = []
        for i in range(len(arr)):
            res.append(rank[arr[i]])

        return res


# Performance Result:
#   Coding Time: 00:05:53
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 400 ms, faster than 14.32%
#   Memory Usage: 31.6 MB, less than 90.53%
