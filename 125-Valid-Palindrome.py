class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = -1
        for left in range(len(s)):
            if not s[left].isalnum():
                continue

            while not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            right -= 1

        return True


# Sample test case:
#   Input:
#       "A man, a plan, a canal: Panama"
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:11:13
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 108 ms, faster than 5.01% of Python3
#       online submissions for Valid Palindrome.
#   Memory Usage: 14.2 MB, less than 46.43% of Python3
#       online submissions for Valid Palindrome.
