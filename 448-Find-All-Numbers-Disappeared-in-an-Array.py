class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for num in nums:
            res[num - 1] += 1

        return [i + 1 for i in range(len(res)) if res[i] == 0]


# Performance Result:
#   Coding Time: 00:05:07
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 460 ms, faster than 30.57%
#   Memory Usage: 21.3 MB, less than 87.38%
