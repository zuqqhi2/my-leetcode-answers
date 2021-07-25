class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_pos = [i for i in range(len(boxes)) if boxes[i] == '1']
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in ball_pos:
                res[i] += abs(i - j)

        return res


# Performance Result:
#   Coding Time: 00:04:40
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 3204 ms, faster than 45.56%
#   Memory Usage: 14.6 MB, less than 47.28%
