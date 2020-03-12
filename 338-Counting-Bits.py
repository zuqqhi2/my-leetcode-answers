class Solution:
    def countBits(self, num: int):
        """
        :rtype List[int]
        """
        # Corner case
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]

        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = bin(i).count('1')

        return result


s = Solution()
print(s.countBits(5))

# Sample test case:
#   Input:
#       11
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:07:31
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 43.91% of Python3
#       online submissions for Counting Bits.
#   Memory Usage: 19.7 MB, less than 5.00% of Python3
#       online submissions for Counting Bits.
