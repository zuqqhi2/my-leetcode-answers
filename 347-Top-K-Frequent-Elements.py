import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        # Create value and its frequency tuple heap
        val_count = defaultdict(int)
        for val in nums:
            val_count[val] += 1
        freq_nums = [(-freq, val) for val, freq in val_count.items()]
        heapq.heapify(freq_nums)

        # Pick up k nums
        result = []
        for i in range(k):
            result.append(heapq.heappop(freq_nums)[1])

        return result


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))


# Sample test case:
#   Input:
#       nums = [1,1,1,2,2,3], k = 2
#   Output:
#       [1,2]

# Performance Result:
#   Coding Time: 00:13:41
#   Time Complexity: O(n log n)
#   Space Complexity: O(n)
#   Runtime: 100 ms, faster than 96.84% of Python3
#       online submissions for Top K Frequent Elements.
#   Memory Usage: 17.1 MB, less than 6.25% of Python3
#       online submissions for Top K Frequent Elements.
