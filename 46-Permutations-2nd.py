class Solution:
    def backtrack(self, nums, cur_result=[]):
        if len(nums) == 0:
            return [cur_result]

        result = []
        created = {}
        for i in range(len(nums)):
            new_nums = nums[:]
            del new_nums[i]
            new_results = self.backtrack(new_nums, cur_result + [nums[i]])

            for res in new_results:
                key = ','.join(map(str, res))
                if key not in created:
                    result.append(res)
                    created[key] = True

        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        # Corner case
        if len(nums) == 0:
            return []

        # Backtracking
        return self.backtrack(nums)


# Performance Result:
#   Coding Time: 00:14:55
#   Time Complexity: O(¥sum^N_{k=1} P(N, k))
#   Space Complexity: O(N!)
#   Runtime: 52 ms, faster than 7.48% of Python3
#       online submissions for Permutations.
#   Memory Usage: 13 MB, less than 96.43% of Python3
#       online submissions for Permutations.
