class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_min_max_pos = {}
        for i in range(len(S)):
            if S[i] not in char_min_max_pos:
                char_min_max_pos[S[i]] = [i, i]
            else:
                char_min_max_pos[S[i]][0] = min(char_min_max_pos[S[i]][0], i)
                char_min_max_pos[S[i]][1] = max(char_min_max_pos[S[i]][1], i)

        res = []
        cnt = 1
        for i in range(1, len(S)):
            is_cross = False
            for c in char_min_max_pos.keys():
                if char_min_max_pos[c][0] < i <= char_min_max_pos[c][1]:
                    is_cross = True
                    break

            if not is_cross:
                res.append(cnt)
                cnt = 0

            cnt += 1

        if cnt > 0:
            res.append(cnt)

        return res


# Performance Result:
#   Coding Time: 00:21:47
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 96 ms, faster than 5.23%
#   Memory Usage: 14.1 MB, less than 99.93%
