class Solution:
    def longestConsecutive(self, nums) -> int:
        """
        :param List[int] nums: unsorted array of integer
        :rtype: int
        :return: length of the longest consecuitive elements sequence
        """
        # Corner case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nexts = {n: -1.1e+6 for n in nums}
        for n in nexts.keys():
            if n - 1 in nexts:
                nexts[n - 1] = n

        max_length = 1
        for n in nexts.keys():
            length = 1
            cur_num = n
            while nexts[cur_num] > -1e+6:
                cur_num = nexts[cur_num]
                length += 1

            if length > max_length:
                max_length = length

        return max_length


# Sample test case:
#   Input:
#       [100, 4, 200, 1, 3, 2]
#   Output:
#       4

# Performance Result:
#   Coding Time: 00:10:43
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 5380 ms, faster than 5.02% of Python3
#       online submissions for Longest Consecutive Sequence.
#   Memory Usage: 14.2 MB, less than 70.37% of Python3
#       online submissions for Longest Consecutive Sequence.
