class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


# Performance Result:
#   Coding Time: 00:02:03
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 58.73%
#   Memory Usage: 14.9 MB, less than 60.80%
