class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_hist = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log_hist:
            self.log_hist[message] = timestamp
            return True
        elif timestamp >= self.log_hist[message] + 10:
            self.log_hist[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# Performance Result:
#   Coding Time: 00:05:48
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 156 ms, faster than 50.86%
#   Memory Usage: 19.8 MB, less than 20.00%
