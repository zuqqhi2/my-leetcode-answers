class Solution:
    def maxArea(self, height) -> int:
        # Corner case
        if height is None:
            return 0
        if len(height) <= 1:
            return 0
        if len(height) == 2:
            return min(height[0], height[1]) * 1

        # 2-pointers
        left_idx = 0
        right_idx = len(height) - 1
        max_cap = 0
        while left_idx <= right_idx:
            cap = (right_idx - left_idx)\
                  * min(height[left_idx], height[right_idx])
            if cap > max_cap:
                max_cap = cap

            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return max_cap


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# Sample test case:
#   Input:
#       [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output:
#       49

# Performance Result:
#   Coding Time: 00:15:06
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 132 ms, faster than 63.64% of Python3
#       online submissions for Container With Most Water.
#   Memory Usage: 14.4 MB, less than 82.11% of Python3
#       online submissions for Container With Most Water.
