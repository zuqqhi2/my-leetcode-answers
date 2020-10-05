class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            top2_val = [stones[0]]
            top2_val_idx = [0]
            if stones[1] > top2_val[0]:
                top2_val.insert(0, stones[1])
                top2_val_idx.insert(0, 1)
            else:
                top2_val.append(stones[1])
                top2_val_idx.append(1)

            for i in range(2, len(stones)):
                if stones[i] > top2_val[0]:
                    top2_val.insert(0, stones[i])
                    top2_val.pop()
                    top2_val_idx.insert(0, i)
                    top2_val_idx.pop()
                elif stones[i] > top2_val[1]:
                    top2_val.insert(1, stones[i])
                    top2_val.pop()
                    top2_val_idx.insert(1, i)
                    top2_val_idx.pop()

            if top2_val[0] > top2_val[1]:
                stones[top2_val_idx[0]] = top2_val[0] - top2_val[1]
                del stones[top2_val_idx[1]]
            elif top2_val[0] == top2_val[1]:
                del stones[top2_val_idx[1]]
                del stones[top2_val_idx[0]]

        return stones[0] if len(stones) >= 1 else 0


# Performance Result:
#   Coding Time: 00:08:15
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 62.09%
#   Memory Usage: 14.2 MB, less than 5.23%
