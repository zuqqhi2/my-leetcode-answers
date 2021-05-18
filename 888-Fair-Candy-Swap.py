class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        ori_sum_a = sum(A)
        ori_sum_b = sum(B)
        set_b = set(B)

        for x in A:
            target = x + (ori_sum_b - ori_sum_a) // 2
            if target in set_b:
                return [x, target]

        return None


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 356 ms, faster than 74.34%
#   Memory Usage: 16.7 MB, less than 50.26%
