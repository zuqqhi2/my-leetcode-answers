import collections
import copy


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        nexts = collections.defaultdict(list)
        for w in words:
            if len(w) <= 1:
                continue

            for i in range(len(w)):
                nexts[w[:i] + "*" + w[i + 1:]].append(w)

        max_len = 1
        for w in words:
            opened = [(w, 1, set())]  # word, length, visited
            while len(opened) > 0:
                cur_w, cur_len, cur_visited = opened.pop(0)
                max_len = max(max_len, cur_len)
                cur_visited.add(cur_w)

                for i in range(len(cur_w) + 1):
                    search_w = cur_w
                    if i < len(cur_w):
                        search_w = search_w[:i] + "*" + search_w[i:]
                    else:
                        search_w = search_w + "*"

                    for nw in nexts[search_w]:
                        if nw in cur_visited:
                            continue
                        opened.append((nw, cur_len + 1, copy.copy(cur_visited)))

        return max_len


# Performance Result:
#   Coding Time: 00:15:11
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 652 ms, faster than 21.99%
#   Memory Usage: 21.1 MB, less than 5.05%
