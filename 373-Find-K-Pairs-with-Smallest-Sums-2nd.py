import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        for i in range(len(nums1)):
            num_pushed = 0
            for j in range(len(nums2)):
                heapq.heappush(ans, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))
                if len(ans) > k:
                    poped_elem = heapq.heappop(ans)
                    if poped_elem[1] == i and poped_elem[2] == j:
                        break

                num_pushed += 1

            if num_pushed == 0:
                break

        res = []
        while len(ans) > 0:
            poped_elem = heapq.heappop(ans)
            res.append([poped_elem[1], poped_elem[2]])

        return list(reversed(res))


# Performance Result:
#   Coding Time: 00:10:09
#   Time Complexity: O(N^2 log N)
#   Space Complexity: O(N)
#   Runtime: 736 ms, faster than 5.28% of Python3
#       online submissions for Find K Pairs with Smallest Sums.
#   Memory Usage: 14 MB, less than 33.33% of Python3
#       online submissions for Find K Pairs with Smallest Sums.
