class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes[:] = sorted(boxTypes, key=lambda x: -x[1])
        score = 0
        for i in range(len(boxTypes)):
            num = min(truckSize, boxTypes[i][0])
            score += num * boxTypes[i][1]
            truckSize -= num
            if truckSize <= 0:
                break

        return score


# Performance Result:
#   Coding Time: 00:08:45
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 160 ms, faster than 36.15%
#   Memory Usage: 14.9 MB, less than 47.24%
