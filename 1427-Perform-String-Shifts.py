class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_amounts = [0, 0]
        for item in shift:
            shift_amounts[item[0]] += item[1]

        is_left = True
        shift_amount = shift_amounts[0] - shift_amounts[1]
        if shift_amounts[1] > shift_amounts[0]:
            is_left = False
            shift_amount = shift_amounts[1] - shift_amounts[0]

        res = ""
        length = len(s)
        for i in range(length):
            shifted_i = (i + shift_amount) % length if is_left else (i - shift_amount) % length
            res += s[shifted_i]

        return res


# Performance Result:
#   Coding Time: 00:07:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 18.48%
#   Memory Usage: 14.3 MB, less than 33.18%
