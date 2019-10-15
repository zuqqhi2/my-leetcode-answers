# diff = no of ways when color of last
#   two posts is different
# same = no of ways when color of last
#   two posts is same
# total ways = diff + sum
#
# for n = 1
#   diff = k, same = 0
#   total = k
#
# for n = 2
#   diff = k * (k-1)  # k choices for first post, k-1 for next
#   same = k  # k choices for common color of two posts
#   total = k +  k * (k-1)
#
# for n = 3
#   diff = [k +  k * (k-1)] * (k-1)
#       (k-1) choices for 3rd post to not have color of 2nd post.
#     same = k * (k-1)
#       c'' != c, (k-1) choices for it
#
# Hence we deduce that,
# total[i] = same[i] + diff[i]
# same[i]  = diff[i-1]
# diff[i]  = (diff[i-1] + diff[i-2]) * (k-1)
#          = total[i-1] * (k-1)


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0

        # Set initial state for DP
        diff = k
        same = 0
        dp = diff + same  # no need to keep all history for this problem

        # Fill for 2 posts onwards
        for i in range(2, n + 1):
            # Current same is same as previous diff
            same = diff

            # We always have k-1 choices for next post
            diff = dp * (k - 1)

            # Total choices till i.
            dp = same + diff

        return dp

# Sample Testcase:
#   Input:
#       n = 3, k = 2
#   Output:
#       6

# Performance Result:
#   Coding Time: 00:28:51
#   Time Complexity: O(nk)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 26.26% of Python3
#       online submissions for Paint Fence.
#   Memory Usage: 13.6 MB, less than 100.00% of Python3
#       online submissions for Paint Fence.
