import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        max_y = len(mat)
        max_x = len(mat[0])

        for y in range(max_y):
            cur_y, cur_x = y, 0
            heap = []
            while cur_y < max_y and cur_x < max_x:
                heapq.heappush(heap, mat[cur_y][cur_x])
                cur_y += 1
                cur_x += 1

            cur_y, cur_x = y, 0
            while cur_y < max_y and cur_x < max_x:
                mat[cur_y][cur_x] = heapq.heappop(heap)
                cur_y += 1
                cur_x += 1

        for x in range(1, max_x):
            cur_y, cur_x = 0, x
            heap = []
            while cur_y < max_y and cur_x < max_x:
                heapq.heappush(heap, mat[cur_y][cur_x])
                cur_y += 1
                cur_x += 1

            cur_y, cur_x = 0, x
            while cur_y < max_y and cur_x < max_x:
                mat[cur_y][cur_x] = heapq.heappop(heap)
                cur_y += 1
                cur_x += 1

        return mat


# Performance Result:
#   Coding Time: 00:10:25
#   Time Complexity: O(MN log(min(N, M)))
#   Space Complexity: O(min(N, M))
#   Runtime: 88 ms, faster than 42.38%
#   Memory Usage: 14.6 MB, less than 53.34%
