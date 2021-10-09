class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates[:] = sorted(coordinates, key=lambda x: x[0] + x[1])
        if coordinates[0][0] == coordinates[1][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
        else:
            a = (coordinates[1][1] - coordinates[0][1]) / (
                    coordinates[1][0] - coordinates[0][0])
            b = coordinates[0][1] - a * coordinates[0][0]
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != int(a * coordinates[i][0]) + b:
                    return False

        return True


# Performance Result:
#   Coding Time: 00:28:19
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 98.20%
#   Memory Usage: 14.7 MB, less than 73.49%
