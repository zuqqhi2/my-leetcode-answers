class Solution:
    def canJump(self, nums) -> bool:
        """
        :param List[int] nums: max jump length array
        :rtype: bool
        :return: Last index can be reached or not
        """
        # Corner cases
        if nums is None:
            return False
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        if len(nums) == 2 and nums[0] != 0:
            return True
        elif len(nums) == 0 and nums[0] == 0:
            return False

        # Dynamic Programming
        #   dp[i]: it can be reached from 0 or not(bool type)
        #   i: nums index
        #   dp[0] = True
        #   dp[i] = True if dp[i - 1]
        reachable = [True] + [False] * (len(nums) - 1)
        for i in range(1, len(nums)):
            for j in range(1, i + 1):
                if reachable[i - j] and nums[i - j] >= j:
                    reachable[i] = True
                    break

        return reachable[-1]


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))

# Sample test case:
#   Input:
#       [3,2,1,0,4]
#   Output:
#       False

# Performance Result:
#   Coding Time: 00:19:02
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 100 ms, faster than 28.48% of Python3
#       online submissions for Jump Game.
#   Memory Usage: 15 MB, less than 7.14% of Python3
#       online submissions for Jump Game.
