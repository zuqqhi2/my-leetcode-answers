class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        len_hand = len(hand)
        if len_hand % W != 0 or len_hand == 0:
            return False

        hand = sorted(hand)

        grouped = [[] for _ in range(len_hand // W)]
        grouped[0].append(hand[0])
        for i in range(1, len_hand):
            is_appended = False
            for j in range(len(grouped)):
                len_j = len(grouped[j])
                if len_j == 0:
                    grouped[j].append(hand[i])
                    is_appended = True
                    break
                elif len_j < W and grouped[j][len_j - 1] + 1 == hand[i]:
                    grouped[j].append(hand[i])
                    is_appended = True
                    break

            if not is_appended:
                return False

        return True


# Performance Result:
#   Coding Time: 00:16:43
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 8936 ms, faster than 5.05%
#   Memory Usage: 15.1 MB, less than 93.22%
