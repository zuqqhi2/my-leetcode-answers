class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num_dist = 0
        while x > 0 or y > 0:
            if x > 0 and y > 0:
                if x & 1 != y & 1:
                    num_dist += 1
            else:
                if x > 0 and x & 1 == 1:
                    num_dist += 1
                elif y > 0 and y & 1 == 1:
                    num_dist += 1

            x = x // 2;
            y = y // 2;

        return num_dist

# Time: 00:10:29
# Runtime: 20 ms
# Memory Usage: 13.7 MB
