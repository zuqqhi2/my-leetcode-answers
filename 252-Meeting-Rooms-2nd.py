class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[1])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:04:28
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 68 ms, faster than 96.74% of Python3
#       online submissions for Valid Palindrome.
#   Memory Usage: 17.1 MB, less than 7.69% of Python3
#       online submissions for Valid Palindrome.
