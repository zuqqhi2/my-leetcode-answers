class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return f'{bulls}A{both - bulls}B'


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 56 ms, faster than 20.26%
#   Memory Usage: 14 MB, less than 25.00%
