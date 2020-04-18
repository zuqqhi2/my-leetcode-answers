class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        intervals = sorted(intervals, key=lambda x: x[1])

        max_room_required = 1
        room_required_list = [1] * len(intervals)
        for i in range(1, len(intervals)):
            for j in reversed(range(0, i)):
                if intervals[i][0] < intervals[j][1]:
                    room_required_list[j] += 1
                    max_room_required = max(max_room_required,
                                            room_required_list[j])
                else:
                    break

        return max_room_required


# Performance Result:
#   Coding Time: 00:22:57
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 84 ms, faster than 34.35%
#   Memory Usage: 17 MB, less than 5.41%
