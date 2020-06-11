import collections


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Corner cases
        if len(source) == 0 and len(target) > 0:
            return -1
        if len(source) > 0 and len(target) == 0:
            return -1
        if len(source) == 0 and len(target) == 0:
            return 0

        char_pos = collections.defaultdict(list)
        for i, c in enumerate(source):
            char_pos[c].append(i)

        prev_c_pos = -1
        num_subsec = 1
        for i in range(len(target)):
            if target[i] not in char_pos:
                return -1

            min_pos = 10000;
            global_min_pos = 10000;
            for p in char_pos[target[i]]:
                global_min_pos = min(global_min_pos, p)
                if p > prev_c_pos:
                    min_pos = min(min_pos, p)

            if min_pos == 10000:
                num_subsec += 1
                prev_c_pos = global_min_pos
            else:
                prev_c_pos = min_pos

        return num_subsec


# Performance Result:
#   Coding Time: 00:20:24
#   Time Complexity: O(N + M)
#   Space Complexity: O(M)
#   Runtime: 88 ms, faster than 12.34%
#   Memory Usage: 14 MB, less than 25.26%
