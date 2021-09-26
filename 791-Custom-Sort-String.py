class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_idx = {order[i]:i for i in range(len(order))}
        return ''.join(list(sorted(s, key=lambda c: order_idx[c] if c in order_idx else len(order))))


# Performance Result:
#   Coding Time: 00:17:42
#   Time Complexity: O(N log N)
#   Space Complexity: O(M)
#   Runtime: 32 ms, faster than 68.92%
#   Memory Usage: 14.2 MB, less than 48.03%
