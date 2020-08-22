class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = []
        odds = []
        for num in A:
            if num % 2 == 0:
                res.append(num)
            else:
                odds.append(num)

        res.extend(odds)
        return res


# Performance Result:
#   Coding Time: 00:01:39
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 108 ms, faster than 34.25%
#   Memory Usage: 14.6 MB, less than 5.43%
