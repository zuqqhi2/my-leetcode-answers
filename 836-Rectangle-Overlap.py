class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        center1 = [(rec1[0] + rec1[2]) / 2, (rec1[1] + rec1[3]) / 2]
        center2 = [(rec2[0] + rec2[2]) / 2, (rec2[1] + rec2[3]) / 2]
        if (abs(center1[0] - center2[0]) < abs(rec1[0] - rec1[2]) / 2 + abs(rec2[0] - rec2[2]) / 2) \
            and (abs(center1[1] - center2[1]) < abs(rec1[1] - rec1[3]) / 2 + abs(rec2[1] - rec2[3]) / 2):
            return True
        else:
            return False


# Performance Result:
#   Coding Time: 00:11:40
#   Time Complexity: O(1)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 9.21%
#   Memory Usage: 13.9 MB, less than 10.00%
