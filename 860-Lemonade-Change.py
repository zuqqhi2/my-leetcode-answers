class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_cnt = [0, 0]  # 5, 10
        for i in range(len(bills)):
            if bills[i] == 5:
                bill_cnt[0] += 1
            elif bills[i] == 10:
                bill_cnt[1] += 1
                bill_cnt[0] -= 1
            else:
                if bill_cnt[1] > 0:
                    bill_cnt[0] -= 1
                    bill_cnt[1] -= 1
                else:
                    bill_cnt[0] -= 3

            if bill_cnt[0] < 0 or bill_cnt[1] < 0:
                return False

        return True


# Performance Result:
#   Coding Time: 00:08:26
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 136 ms, faster than 75.58%
#   Memory Usage: 14.6 MB, less than 5.97%
