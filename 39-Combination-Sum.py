# Algorithm: Backtracking


class Solution:
    def backtrack(self, candidates, arr, remain, pos=0):
        if pos == len(candidates) and remain == 0:
            return [arr]
        elif pos == len(candidates):
            return []

        result = []

        sub_res = self.backtrack(candidates, arr, remain, pos + 1)
        result += sub_res

        if remain >= candidates[pos]:
            result += self.backtrack(candidates, arr + [candidates[pos]], remain - candidates[pos], pos)

        return result

    def combinationSum(self, candidates, target: int):
        if candidates is None:
            return None
        elif len(candidates) == 0:
            return []
        elif len(candidates) == 1 and target % candidates[0] >= 1:
            return []

        return self.backtrack(candidates, [], target, 0)


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))


# Sample test case:
#   Input:
#       candidates = [2,3,6,7], target = 7
#   Output:
#   [
#      [7],
#      [2,2,3]
#   ]

# Performance Result:
#   Coding Time: 00:20:26
#   Time Complexity: O(n)
#   Space Complexity: O(m^n)
#   Runtime: 112 ms, faster than 38.93% of Python3
#       online submissions for Combination Sum.
#   Memory Usage: 13.5 MB, less than 7.57% of Python3
#       online submissions for Combination Sum.
