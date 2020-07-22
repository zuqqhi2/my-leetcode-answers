class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hash[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hash[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Performance Result:
#   Coding Time: 00:02:36
#   Time Complexity: O(1)
#   Space Complexity: O(N)
#   Runtime: 1520 ms, faster than 10.47%
#   Memory Usage: 39.8 MB, less than 5.09%
