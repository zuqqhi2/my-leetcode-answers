class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        history = {num:i + 1 for i, num in enumerate(numbers)}
        for i in range(len(numbers)):
            j = i + 1
            needed_num = target - numbers[i]
            if needed_num in history:
                return [j, history[needed_num]] if history[needed_num] > j else [history[needed_num], j]


# Performance Result:
#   Coding Time: 00:04:45
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 78.32%
#   Memory Usage: 14.4 MB, less than 30.66%
