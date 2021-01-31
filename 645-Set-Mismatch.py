import collections


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = collections.defaultdict(int)
        dup_num = 0
        for num in nums:
            counts[num] += 1
            if counts[num] >= 2:
                dup_num = num

        res = [dup_num]
        for num in range(1, len(nums) + 1):
            if num not in counts:
                res.append(num)
                break

        return res


# Performance Result:
#   Coding Time: 00:04:42
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 328 ms, faster than 13.18%
#   Memory Usage: 15.9 MB, less than 41.76%
