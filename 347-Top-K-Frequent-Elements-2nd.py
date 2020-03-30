import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        heap = []
        for key, cnt in counts.items():
            heapq.heappush(heap, (-cnt, key))

        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result


# Performance Result:
#   Coding Time: 00:07:53
#   Time Complexity: O(N log N)
#   Space Complexity: O(n)
#   Runtime: 100 ms, faster than 89.79% of Python3
#       online submissions for Top K Frequent Elements.
#   Memory Usage: 17.5 MB, less than 6.25% of Python3
#       online submissions for Top K Frequent Elements.
