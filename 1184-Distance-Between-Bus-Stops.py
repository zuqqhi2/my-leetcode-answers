class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        # Clockwise
        dist = 0
        idx = start
        while idx != destination:
            dist += distance[idx]
            idx = (idx + 1) % len(distance)

        # Counter Clockwise
        ccw_dist = 0
        idx = start
        while idx != destination:
            idx = (idx - 1) % len(distance)
            ccw_dist += distance[idx]

        return min(dist, ccw_dist)


# Performance Result:
#   Coding Time: 00:07:48
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 44 ms, faster than 85.82%
#   Memory Usage: 15.1 MB, less than 74.59%
