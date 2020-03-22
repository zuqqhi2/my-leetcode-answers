class Solution:
    def merge(self, intervals):
        """
        :param List[List[int]] intervals:
        :rtype: List[List[int]]
        :return:
        """
        # Corner case
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])

        prev_idx = 0
        for i in range(1, len(intervals)):
            if max(intervals[prev_idx][0], intervals[i][0]) \
                <= min(intervals[prev_idx][1], intervals[i][1]):
                intervals[prev_idx][1] = max(intervals[prev_idx][1], intervals[i][1])
                intervals[i] = None
            else:
                prev_idx = i

        return [interval for interval in intervals if interval is not None]


# Sample test case:
#   Input:
#       [[1,3],[2,6],[8,10],[15,18]]
#   Output:
#       [[1,6],[8,10],[15,18]]

# Performance Result:
#   Coding Time: 00:08:38
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 100 ms, faster than 20.38% of Python3 online submissions for Merge Intervals.
#   Memory Usage: 14.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
