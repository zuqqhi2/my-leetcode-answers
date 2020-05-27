class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                remove_l_s = s[:l] + s[l+1:]
                remove_r_s = s[:r] + s[r+1:]
                return remove_l_s == remove_l_s[::-1] or remove_r_s == remove_r_s[::-1]
        return True


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 100 ms, faster than 88.98%
#   Memory Usage: 14.4 MB, less than 6.25%
