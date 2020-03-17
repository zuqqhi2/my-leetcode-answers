import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Corner case
        if len(words) == 0:
            return ""

        chars = set("".join(words))
        degrees = {x: 0 for x in chars}
        graph = collections.defaultdict(list)
        for pair in zip(words, words[1:]):
            for x, y in zip(*pair):
                if x != y:
                    graph[x].append(y)
                    degrees[y] += 1
                    break

        queue = list(filter(lambda x: degrees[x] == 0, degrees.keys()))
        ret = ""
        while queue:
            x = queue.pop()
            ret += x
            for n in graph[x]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    queue.append(n)

        return ret * (set(ret) == chars)


# Sample test case:
#   Input:
#       [
#           "wrt",
#           "wrf",
#           "er",
#           "ett",
#           "rftt"
#       ]
#   Output:
#       "wertf"

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 89.05% of Python3
#       online submissions for Alien Dictionary.
#   Memory Usage: 12.7 MB, less than 100.00% of Python3
#       online submissions for Alien Dictionary.
