class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1

        if key in self.cache:
            self.cache[key][1] = self.time
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1

        self.cache[key] = [value, self.time]
        if len(self.cache.keys()) > self.cap:
            min_time = 1_000_000
            min_key = -1
            for k in self.cache.keys():
                if self.cache[k][1] < min_time:
                    min_key = k
                    min_time = self.cache[k][1]

            del self.cache[min_key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Performance Result:
#   Coding Time: 00:12:10
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1316 ms, faster than 5.00%
#   Memory Usage: 22.9 MB, less than 77.34%
