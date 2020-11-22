import heapq


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def heuristic(pos, goal):
            return ((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2) ** 0.5

        moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1),
                 (-1, -2)]

        init_pos = (0, 0)
        goal = (x, y)

        passed_list = [init_pos]
        init_score = len(passed_list) + heuristic(init_pos, goal)
        checked = {init_pos: init_score}
        searching_heap = []
        heapq.heappush(searching_heap, (init_score, passed_list))

        while len(searching_heap) > 0:
            score, passed_list = heapq.heappop(searching_heap)
            last_passed_pos = passed_list[-1]
            if last_passed_pos == goal:
                return len(passed_list) - 1

            for move in moves:
                new_pos = (
                last_passed_pos[0] + move[0], last_passed_pos[1] + move[1])
                new_passed_list = passed_list + [new_pos]
                pos_score = len(new_passed_list) + heuristic(new_pos, goal)
                if new_pos in checked and checked[new_pos] <= pos_score:
                    continue

                checked[new_pos] = pos_score
                heapq.heappush(searching_heap, (pos_score, new_passed_list))

        return 0


# Performance Result:
#   Coding Time: 00:16:03
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 60 ms, faster than 78.72%
#   Memory Usage: 15 MB, less than 84.68%
