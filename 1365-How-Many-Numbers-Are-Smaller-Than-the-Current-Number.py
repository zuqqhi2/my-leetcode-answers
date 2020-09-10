class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1

            res.append(cnt)

        return res


# Performance Result:
#   Coding Time: 00:08:39
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 440 ms, faster than 29.92%
#   Memory Usage: 13.9 MB, less than 64.47%
