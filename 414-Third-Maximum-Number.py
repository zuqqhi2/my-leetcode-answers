import heapq
import collections


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_cnt = collections.Counter(nums)
        heap = []
        maximum = 0
        for num in nums_cnt.keys():
            heapq.heappush(heap, num)
            maximum = max(maximum, num)
            if len(heap) > 3:
                heapq.heappop(heap)

        return heapq.heappop(heap) if len(heap) == 3 else maximum


# Performance Result:
#   Coding Time: 00:03:32
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 56 ms, faster than 57.79%
#   Memory Usage: 15 MB, less than 50.18%
