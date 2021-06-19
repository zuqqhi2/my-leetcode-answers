import collections


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        both_likes = list(set(list1) & set(list2))
        least_indexes = collections.defaultdict(list)
        min_sum = 1_000_000
        for shop in both_likes:
            index_sum = list1.index(shop) + list2.index(shop)
            least_indexes[index_sum].append(shop)
            min_sum = min(min_sum, index_sum)

        return least_indexes[min_sum]


# Performance Result:
#   Coding Time: 00:09:29
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 184 ms, faster than 43.45%
#   Memory Usage: 14.7 MB, less than 68.77%
