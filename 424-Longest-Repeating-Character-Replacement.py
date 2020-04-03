class Solution:
    def characterReplacement(self, s, k):
            count = collections.Counter()
            start = result = 0
            for end in range(len(s)):
                count[s[end]] += 1
                max_count = count.most_common(1)[0][1]
                if end - start + 1 - max_count > k:
                    count[s[start]] -= 1
                    start += 1
                result = max(result, end - start + 1)
            return result


# Sample test case:
#   Input:
#       s = "ABAB", k = 2
#   Output:
#       4

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 336 ms, faster than 15.72% of Python3
#       online submissions for Longest Repeating Character Replacement.
#   Memory Usage: 14 MB, less than 12.50% of Python3
#       online submissions for Longest Repeating Character Replacement.
