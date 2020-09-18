import collections
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = [(-freq, word) for word, freq in
                 collections.Counter(words).items()]
        heap = []
        for elem in freqs:
            heapq.heappush(heap, elem)

        res = []
        prev_freq = 0
        tmp = []
        for i in range(k):
            freq = heapq.heappop(heap)
            if freq[0] == prev_freq:
                tmp.append(freq[1])
            else:
                prev_freq = freq[0]
                res.extend(sorted(tmp))
                tmp = [freq[1]]
        if len(tmp) > 0:
            res.extend(tmp)

        return res


# Performance Result:
#   Coding Time: 00:17:29
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 99.81%
#   Memory Usage: 13.8 MB, less than 66.96%
