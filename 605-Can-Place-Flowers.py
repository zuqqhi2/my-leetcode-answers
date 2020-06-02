class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            is_valid = True
            for j in range(max(0, i - 1), min(len(flowerbed), i + 2)):
                if flowerbed[j] == 1:
                    is_valid = False
                    break
            if is_valid:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
        if n > 0:
            return False
        else:
            return True


# Performance Result:
#   Coding Time: 00:18:30
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 220 ms, faster than 17.77%
#   Memory Usage: 13.9 MB, less than 16.67%
