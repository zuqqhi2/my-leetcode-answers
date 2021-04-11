import collections


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnts = collections.Counter(arr)

        cur_missing_cnt = 0
        cur_missing_num = 0
        for i in range(1, 2001):
            if i not in cnts:
                cur_missing_cnt += 1
                cur_missing_num = i
                if cur_missing_cnt == k:
                    break

        return cur_missing_num


# Performance Result:
#   Coding Time: 00:06:08
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 58.64%
#   Memory Usage: 14.2 MB, less than 88.63%
