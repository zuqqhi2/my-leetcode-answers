class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.num_keep = size
        self.history = []

    def next(self, val: int) -> float:
        self.history.append(val)
        if len(self.history) > self.num_keep:
            self.history.pop(0)
        return sum(self.history) / float(len(self.history))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# Performance Result:
#   Coding Time: 00:02:43
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 104 ms, faster than 33.35%
#   Memory Usage: 16.7 MB, less than 9.52%
