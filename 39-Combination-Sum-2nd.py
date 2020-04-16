class Solution:
    def findCombs(self, candidates: List[int], target: int, pos: int = 0,
                  cur_res: List[int] = []) -> List[List[int]]:
        if pos >= len(candidates):
            if target == 0:
                return [cur_res]
            else:
                return []

        result = []
        # Go to next
        result.extend(self.findCombs(candidates, target, pos + 1, cur_res))
        # Use this num
        if target - candidates[pos] >= 0:
            result.extend(self.findCombs(candidates, target - candidates[pos],
                                         pos, cur_res + [candidates[pos]]))

        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        return [e for e in self.findCombs(candidates, target) if len(e) > 0]


# Performance Result:
#   Coding Time: 00:16:12
#   Time Complexity: O(?)
#   Space Complexity: O(?)
#   Runtime: 96 ms, faster than 42.56%
#   Memory Usage: 13.6 MB, less than 7.57%
