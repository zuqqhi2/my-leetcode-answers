class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = []
        evens = []
        for num in A:
            if num % 2 == 0:
                odds.append(num)
            else:
                evens.append(num)

        odds[:] = sorted(odds)
        evens[:] = sorted(evens)

        res = []
        for i in range(len(A)):
            if i % 2 == 0:
                res.append(odds.pop(0))
            else:
                res.append(evens.pop(0))

        return res


# Performance Result:
#   Coding Time: 00:07:28
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 284 ms, faster than 16.62%
#   Memory Usage: 16.5 MB, less than 37.59%
