class SparseVector:
    def __init__(self, nums: List[int]):
        self.pos_values = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                self.pos_values[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pos1 = set(self.pos_values.keys())
        pos2 = set(vec.pos_values.keys())
        targets = list(pos1 & pos2)

        res = 0
        for p in targets:
            res += self.pos_values[p] * vec.pos_values[p]

        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


# Performance Result:
#   Coding Time: 00:06:37
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1724 ms, faster than 94.59%
#   Memory Usage: 18.7 MB, less than 22.91%
