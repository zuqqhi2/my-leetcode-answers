import collections
import heapq


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        freq_heap = []
        for k in freq:
            heapq.heappush(freq_heap, ((freq[k], -k), k))

        res = []
        while len(freq_heap) > 0:
            freq_item = heapq.heappop(freq_heap)
            res.extend([freq_item[1] for _ in range(freq_item[0][0])])

        return res


# Performance Result:
#   Coding Time: 00:14:12
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 53.20%
#   Memory Usage: 14.3 MB, less than 22.97%
