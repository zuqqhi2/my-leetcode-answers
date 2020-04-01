class Solution:
    def generate_power_set(self, nums, cur_pos=0, cur_res=[]) -> List[
        List[int]]:
        if cur_pos >= len(nums):
            return [cur_res]

        # Skip or using cur idx value
        results = self.generate_power_set(nums, cur_pos + 1, cur_res)
        results.extend(self.generate_power_set(nums, cur_pos + 1,
                                               cur_res + [nums[cur_pos]]))

        # Remove duplicates at last
        if cur_pos == 0:
            generated = {}
            for i in range(len(results)):
                key = "key:" + (','.join(map(str, results[i])))
                if key in generated:
                    results[i] = None
                else:
                    generated[key] = True

        return [res for res in results if res is not None]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.generate_power_set(sorted(nums))


# Sample test case:
#   Input:
#       [1,2,2]
#   Output:
#       [
#           [2],
#           [1],
#           [1,2,2],
#           [2,2],
#           [1,2],
#           []
#       ]

# Performance Result:
#   Coding Time: 00:16:39
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 67.38% of Python3
#       online submissions for Subsets II.
#   Memory Usage: 14.2 MB, less than 6.38% of Python3
#       online submissions for Subsets II.
