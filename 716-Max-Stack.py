class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        max_val = self.peekMax()
        self.stack.remove(max_val)
        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


# Performance Result:
#   Coding Time: 00:11:25
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 164 ms, faster than 75.79%
#   Memory Usage: 16.3 MB, less than 25.00%
