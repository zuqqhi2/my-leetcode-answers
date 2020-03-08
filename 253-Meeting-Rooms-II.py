from operator import itemgetter


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if intervals is None:
            return 0
        if len(intervals) == 0:
            return 0

        # sort for easy to find intersection of times
        intervals.sort(key=itemgetter(0))

        mtgs = [[intervals[0]]]
        for mtg_idx in range(1, len(intervals)):
            is_new_room_required = True
            for room_idx in range(len(mtgs)):
                if intervals[mtg_idx][0] >= mtgs[room_idx][-1][1]:
                    mtgs[room_idx].append(intervals[mtg_idx])
                    is_new_room_required = False
                    break

            if is_new_room_required:
                mtgs.append([intervals[mtg_idx]])

        return len(mtgs)


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))
print(s.minMeetingRooms([[5, 20], [0, 30], [15, 25]]))
print(s.minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
print(s.minMeetingRooms([[4, 18], [1, 35], [12, 45], [25, 46], [22, 27]]))
print(s.minMeetingRooms([[1293, 2986], [848, 3846], [4284, 5907],
                         [4466, 4781], [518, 2918], [300, 5870]]))

# Sample test case:
#   Input:
#       [[0, 30],[5, 10],[15, 20]]
#   Output:
#       2

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 148 ms, faster than 5.04% of Python3
#       online submissions for Meeting Rooms II.
#   Memory Usage: 16.1 MB, less than 5.41% of Python3
#       online submissions for Meeting Rooms II.
