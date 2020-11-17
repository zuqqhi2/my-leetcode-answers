import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        num_keys = 0
        occurrences = set()
        for k in cnt.keys():
            num_keys += 1
            occurrences.add(cnt[k])

        return num_keys == len(occurrences)


# Performance Result:
#   Coding Time: 00:03:20
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 59.23%
#   Memory Usage: 14.3 MB, less than 60.26%
