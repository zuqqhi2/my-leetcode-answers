class Solution:
    def minOperations(self, s: str) -> int:
        prev_char = s[0]
        num_required_change = 0
        for i in range(1, len(s)):
            if s[i] == prev_char:
                num_required_change += 1
                prev_char = '0' if s[i] == '1' else '1'
            else:
                prev_char = s[i]

        new_s = '0' if s[0] == '1' else '1'
        new_s += s[1:]
        prev_char = new_s[0]
        num_required_change2 = 1
        for i in range(1, len(new_s)):
            if new_s[i] == prev_char:
                num_required_change2 += 1
                prev_char = '0' if new_s[i] == '1' else '1'
            else:
                prev_char = new_s[i]

        return min(num_required_change, num_required_change2)


# Performance Result:
#   Coding Time: 00:17:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 56 ms, faster than 59.49%
#   Memory Usage: 14.3 MB, less than 88.73%
