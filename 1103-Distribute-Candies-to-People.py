class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        idx = 0
        cnt = 1
        while candies >= 1:
            res[idx] += min(cnt, candies)
            candies -= cnt
            cnt += 1
            idx = (idx + 1) % num_people

        return res


# Performance Result:
#   Coding Time: 00:04:23
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 25.89%
#   Memory Usage: 14.1 MB, less than 15.42%
