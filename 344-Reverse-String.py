class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for i in range(s_len // 2):
            left = i
            right = s_len - 1 - i
            s[left], s[right] = s[right], s[left]


# Performance Result:
#   Coding Time: 00:01:14
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 204 ms, faster than 92.33%
#   Memory Usage: 18.2 MB, less than 84.24%
