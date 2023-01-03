class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = [(heights[i], names[i]) for i in range(len(names))]
        persons = sorted(persons, key=lambda x: -x[0])
        return [persons[i][1] for i in range(len(persons))]


# Performance Result:
#   Coding Time: 00:02:37
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 249 ms, faster than 51.71%
#   Memory Usage: 14.5 MB, less than 10.30%
