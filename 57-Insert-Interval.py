class Solution:
    def insert(self, intervals, newInterval):
        """
        :param List[List[int]] intervals:
        :param List[int] newInterval:
        :rtype: List[List[int]]
        :return:
        """
        # Corner case
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals

        #
        is_expanded = False
        expanded_idx = -1
        for i in range(len(intervals)):
            # No overlap after this element
            if intervals[i][0] > newInterval[1]:
                if not is_expanded:
                    intervals.insert(i, newInterval)
                return [elem for elem in intervals if elem is not None]

            # Overlap check
            max_start = max(intervals[i][0], newInterval[0])
            min_end = min(intervals[i][1], newInterval[1])
            if max_start > min_end:
                continue

            # Merge or just expand or include
            if not is_expanded:
                intervals[i][0] = min(intervals[i][0], newInterval[0])
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                is_expanded = True
                expanded_idx = i
            else:
                intervals[expanded_idx][1] = max(intervals[expanded_idx][1], intervals[i][1])
                intervals[i] = None

        if is_expanded:
            return [elem for elem in intervals if elem is not None]
        else:
            intervals.append(newInterval)
            return intervals


s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


# Sample test case:
#   Input:
#       intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output:
#       [[1,2],[3,10],[12,16]]

# Performance Result:
#   Coding Time: 00:30:53
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 76 ms, faster than 90.68% of Python3
#       online submissions for Insert Interval.
#   Memory Usage: 16.2 MB, less than 8.00% of Python3
#       online submissions for Insert Interval.
