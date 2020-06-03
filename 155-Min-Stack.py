class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.insert(0, (x, x))
        else:
            self.stack.insert(0, (x, min(x, self.stack[0][1])))

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(1)
#   Space Complexity: O(N)
#   Runtime: 76 ms, faster than 36.71%
#   Memory Usage: 18 MB, less than 5.36%
