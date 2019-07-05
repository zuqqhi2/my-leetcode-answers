import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Can't return any pair
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        # Generate heaptree
        candidates = [[v1 + v2, v1, v2] for v1 in nums1 for v2 in nums2]
        heap = []
        for pair in candidates:
            heapq.heappush(heap, pair)

        # Return smallest pair
        result = []
        for attempt in range(k):
            try:
                pair = heapq.heappop(heap)
                result.append([pair[1], pair[2]])
            except IndexError as e:
                break
        return result

# Sample Testcase:
#   Input:
#     nums1 = [1,7,11], nums2 = [2,4,6], k = 3
#   Output:
#     [[1,2],[1,4],[1,6]]

# Performance Result:
#   Coding Time: 00:14:00
#   Runtime: 364 ms, faster than 19.76% of Python3 online submissions for Find K Pairs with Smallest Sums.
#   Memory Usage: 46.7 MB, less than 8.98% of Python3 online submissions for Find K Pairs with Smallest Sums.
