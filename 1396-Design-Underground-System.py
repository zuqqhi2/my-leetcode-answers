import collections


class Traveler:
    def __init__(self, id=0, src='', dest='', src_time=0, dest_time=0):
        self.id = id
        self.src = src
        self.dest = dest
        self.src_time = src_time
        self.dest_time = dest_time


class UndergroundSystem:

    def __init__(self):
        self.src_travelers = collections.defaultdict(list)
        self.id_travelers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        t = Traveler(id, stationName, '', t, 0)
        self.src_travelers[stationName].append(t)
        self.id_travelers[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.id_travelers[id].dest = stationName
        self.id_travelers[id].dest_time = t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sum_time = 0.0
        num_t = 0
        for t in self.src_travelers[startStation]:
            if t.dest == endStation:
                sum_time += t.dest_time - t.src_time
                num_t += 1

        return sum_time / num_t

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# Performance Result:
#   Coding Time: 00:11:06
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 356 ms, faster than 5.20%
#   Memory Usage: 25 MB, less than 9.19%
