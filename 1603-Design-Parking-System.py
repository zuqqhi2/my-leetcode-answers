class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


# Performance Result:
#   Coding Time: 00:03:47
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 136 ms, faster than 71.27%
#   Memory Usage: 14.7 MB, less than 55.20%
