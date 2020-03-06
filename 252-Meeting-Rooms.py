class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        if intervals is None:
            return True
        if len(intervals) == 0:
            return True

        available_times = [False for i in range(1000000)]
        for mtg_start_end in intervals:
            for mtg_time in range(mtg_start_end[0], mtg_start_end[1]):
                if available_times[mtg_time]:
                    return False
                else:
                    available_times[mtg_time] = True

        return True


s = Solution()
print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(s.canAttendMeetings([[7, 10], [2, 4]]))

# Sample test case:
#   Input:
#       weights = [1,2,3,4,5,6,7,8,9,10], D = 5
#   Output:
#       15

# Performance Result:
#   Coding Time: 00:06:51
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 2728 ms, faster than 5.20% of Python3
#       online submissions for Meeting Rooms.
#   Memory Usage: 23.5 MB, less than 7.69% of Python3
#       online submissions for Meeting Rooms.
