class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        """
        :param List[List[int]] intervals:
        :rtype: int
        :return:
        """
        # Corner case
        if len(intervals) <= 1:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        # Greedy
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1

        return len(intervals) - count


s = Solution()
print(s.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))


# Sample test case:
#   Input:
#       [[1,2],[2,3],[3,4],[1,3]]
#   Output:
#       1

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 72 ms, faster than 68.47% of Python3
#       online submissions for Non-overlapping Intervals.
#   Memory Usage: 16 MB, less than 25.00% of Python3
#       online submissions for Non-overlapping Intervals.
