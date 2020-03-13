class Solution:
    def reverseBits(self, n: int) -> int:
        """
        :param int n: input
        :rtype: int
        :return: answer
        """
        is_first_zeros = True
        num_first_zeros = 0
        result = n & 1
        if result == 0:
            num_first_zeros = 1
        else:
            is_first_zeros = False

        while n > 1:
            n = n >> 1
            result = result << 1

            target = n & 1
            result = result ^ target

            if is_first_zeros:
                if target == 0:
                    num_first_zeros += 1
                else:
                    is_first_zeros = False

        cur_len = len(format(result, 'b'))
        if cur_len + num_first_zeros < 32:
            for i in range(32 - cur_len - num_first_zeros):
                result <<= 1

        return result


s = Solution()
target = 43261596
result = s.reverseBits(43261596)
print(target, format(target, 'b'))
print(result, format(result, 'b'))


# Sample test case:
#   Input:
#       [3,0,1]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:22:12
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 77.08% of Python3
#       online submissions for Reverse Bits.
#   Memory Usage: 12.8 MB, less than 100.00% of Python3
#       online submissions for Reverse Bits.
