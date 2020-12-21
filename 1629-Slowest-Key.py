class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations = [releaseTimes[0]]
        max_duration = durations[0]
        for i in range(1, len(releaseTimes)):
            durations.append(releaseTimes[i] - releaseTimes[i - 1])
            max_duration = max(max_duration, durations[i])

        max_keys = []
        for i in range(len(releaseTimes)):
            if durations[i] == max_duration:
                max_keys.append(keysPressed[i])

        max_keys = sorted(max_keys)
        return max_keys[-1]


# Performance Result:
#   Coding Time: 00:05:59
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 31.67%
#   Memory Usage: 14.5 MB, less than 24.93%
