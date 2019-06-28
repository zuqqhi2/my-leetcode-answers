class Solution:
    __digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    __int_max = int(2 ** 31 - 1)
    __int_min = int(-2 ** 31)

    def myAtoi(self, str: str) -> int:
        """
        :type str: string to be converted to integer

        Time complexity: O(n)
        Space complexity: O(1)
        """
        result_int = 0
        started_number_flg = False
        prefix_space = True
        sign_specified_flg = False
        sign = 1
        for idx, c in enumerate(str):
            # Check head white spaces
            if prefix_space and c != ' ':
                prefix_space = False

            if not prefix_space:
                # Minus sign
                if not started_number_flg and not sign_specified_flg and c == '-':
                    sign_specified_flg = True
                    sign = -1
                elif not started_number_flg and not sign_specified_flg and c == '+':
                    sign_specified_flg = True
                    sign = 1
                # Digit
                elif c in self.__digits.keys():
                    if not started_number_flg:
                        started_number_flg = True
                    result_int = result_int * 10 + self.__digits[c]
                # Not digit
                else:
                    break

        if started_number_flg:
            result_int *= sign
            if result_int < self.__int_min:
                return self.__int_min
            elif result_int > self.__int_max:
                return self.__int_max
            else:
                return result_int
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("+1"))

# Sample Testcase:
#   Input:
#     "   -42"
#   Output:
#     -42

# Performance Result:
#   Coding Time: 00:39:00
#   Runtime: 40 ms, faster than 85.33% of Python3 online submissions for String to Integer (atoi).
#   Memory Usage: 13.2 MB, less than 56.06% of Python3 online submissions for String to Integer (atoi).
