import collections


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        boxes = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            if len(boxes[groupSizes[i]]) == 0:
                boxes[groupSizes[i]].append([])

            cur_box_id = 0
            while cur_box_id < len(boxes[groupSizes[i]]) and len(
                boxes[groupSizes[i]][cur_box_id]) >= groupSizes[i]:
                cur_box_id += 1

            if cur_box_id >= len(boxes[groupSizes[i]]):
                boxes[groupSizes[i]].append([i])
            else:
                boxes[groupSizes[i]][cur_box_id].append(i)

        res = []
        for k in boxes.keys():
            res.extend(boxes[k])

        return res


# Performance Result:
#   Coding Time: 00:14:15
#   Time Complexity: O(NH)
#   Space Complexity: O(N)
#   Runtime: 252 ms, faster than 5.16%
#   Memory Usage: 14.4 MB, less than 48.47%
