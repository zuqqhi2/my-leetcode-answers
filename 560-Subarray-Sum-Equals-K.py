class Solution:
    def subarraySum(self, nums, k):
        cnt = { 0: 1 }
        total = 0
        k_count = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in cnt:
                k_count += cnt[total - k]

            if total not in cnt:
                cnt[total] = 1
            else:
                cnt[total] += 1

        return k_count


s = Solution()
print(s.subarraySum([1, 1, 1], 2)) # 2
print(s.subarraySum([], 2)) # 0
print(s.subarraySum([1, 3, 2, 4], 6)) # 2
print(s.subarraySum([3, -3, 2, 4, -2, 1, -3, -2], 0)) # 4
print(s.subarraySum([0,0,0,0,0,0,0,0,0,0], 0)) # 55


# Sample test case:
#   Input:
#       nums = [1,1,1], k = 2
#   Output:
#       2

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 112 ms, faster than 93.48% of Python3
#       online submissions for Subarray Sum Equals K.
#   Memory Usage: 15.1 MB, less than 96.00% of Python3
#       online submissions for Subarray Sum Equals K.
