class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Arrenge number of digits
        len_a = len(a)
        len_b = len(b)
        max_len = len_a
        if len_b > len_a:
            max_len = len_b
            a = '0' * (max_len - len_a) + a
        else:
            b = '0' * (max_len - len_b) + b
        
        # Process for each digit
        result = ''
        carrige = '0'
        for op1, op2 in zip(reversed(a), reversed(b)):
            value = int(op1) + int(op2) + int(carrige)
            
            # Decide carrige
            if value >= 2:
                carrige = '1'
            else:
                carrige = '0'

            # Decide current digit
            if value == 1 or value == 3:
                result += '1'
            else:
                result += '0'
        
        # carrige is '1' after last digit processing
        # Add one more digit
        if carrige == '1':
            result += '1'
        
        # result is reserved so fix it
        return ''.join(list(reversed(result)))

# Debug code
#s = Solution()
#print(s.addBinary('11', '1')) # 100
#print(s.addBinary('1010', '1011')) # 10101


# Sample Testcase:
#   Input:
#     a = "11", b = "1"
#   Output:
#     "100"

# Performance Result:
#   Coding Time: 00:20:00
#   Runtime: 48 ms, faster than 18.73% of Python3 online submissions for Add Binary.
#   Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Add Binary.