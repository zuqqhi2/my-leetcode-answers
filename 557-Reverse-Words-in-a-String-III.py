class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split(' ')
        for i in range(len(strs)):
            strs[i] = ''.join(list(reversed(strs[i])))

        return ' '.join(strs)


# Performance Result:
#   Coding Time: 00:01:48
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 80 ms, faster than 17.93%
#   Memory Usage: 14.2 MB, less than 72.46%
