class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True

# Time: 27:49
# Runtime: 32 ms
# Memory Usage: 13.7 MB
