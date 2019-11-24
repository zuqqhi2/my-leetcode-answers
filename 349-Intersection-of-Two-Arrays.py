class Solution:
    def intersection(self, nums1, nums2):
        num1_hash = {}
        for num in nums1:
            num1_hash[num] = True

        result = []
        for num in nums2:
            if num in num1_hash:
                result.append(num)

        return set(result)


# Sample test case:
#   Input:
#       nums1 = [1,2,2,1], nums2 = [2,2]
#   Output:
#       [2]

# Performance Result:
#   Coding Time: 00:03:43
#   Time Complexity: O(N + M)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 100.00% of Python3
#       online submissions for Intersection of Two Arrays.
#   Memory Usage: 12.7 MB, less than 100.00% of Python3
#       online submissions for Intersection of Two Arrays.
