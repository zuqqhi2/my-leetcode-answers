class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [False for _ in range(1_000_000)]

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        self.hash[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Performance Result:
#   Coding Time: 00:02:03
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1148 ms, faster than 17.05%
#   Memory Usage: 41.9 MB, less than 5.36%
