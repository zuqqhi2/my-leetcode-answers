class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        groupA = []
        groupB = []
        for i in range(len(costs)):
            if costs[i][0] > costs[i][1]:
                groupB.append(costs[i])
            else:
                groupA.append(costs[i])
        print(groupA, groupB)

        target = groupA
        other = groupB
        if len(groupB) > len(groupA):
            target = groupB
            other = groupA

        for i in range(len(target)):
            target[i].append(abs(target[i][0] - target[i][1]))
        target = sorted(target, key=lambda x: x[2])

        num_required = len(costs) // 2
        for i in range(num_required - len(other)):
            other.append(target[i][:])
            target[i][:] = []

        costA = sum([num[0] for num in groupA if len(num) >= 2])
        costB = sum([num[1] for num in groupB if len(num) >= 2])

        return costA + costB


# Performance Result:
#   Coding Time: 00:29:06
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 87.68%
#   Memory Usage: 14.1 MB, less than 5.06%
