import collections


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')[:2]
            dom_elements = domain.split('.')
            for i in reversed(range(len(dom_elements))):
                counts['.'.join(dom_elements[i:])] += int(cnt)

        res = []
        for key in counts.keys():
            res.append(str(counts[key]) + ' ' + key)

        return res


# Performance Result:
#   Coding Time: 00:07:57
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 86.54%
#   Memory Usage: 14.1 MB, less than 14.78%
