class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        len1 = len(num1)
        len2 = len(num2)
        max_len = max(len1, len2)
        carry = 0
        for i in range(max_len):
            sub_result = carry
            if i < len1:
                sub_result += int(num1[len1 - 1 - i])
            if i < len2:
                sub_result += int(num2[len2 - 1 - i])
            if sub_result >= 10:
                carry = sub_result // 10
                sub_result = sub_result % 10
            else:
                carry = 0
            result.insert(0, str(sub_result))
        if carry > 0:
            result.insert(0, str(carry))

        return ''.join(result)


# Performance Result:
#   Coding Time: 00:22:51
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 45.42%
#   Memory Usage: 14.1 MB, less than 5.55%
