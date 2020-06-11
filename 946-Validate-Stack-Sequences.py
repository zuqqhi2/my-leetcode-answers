class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        isPushed = set()
        stack = []
        pop_idx = 0
        push_idx = 0
        while pop_idx < len(popped):
            while popped[pop_idx] not in isPushed and push_idx < len(pushed):
                stack.insert(0, pushed[push_idx])
                isPushed.add(pushed[push_idx])
                push_idx += 1

            if stack.pop(0) == popped[pop_idx]:
                pop_idx += 1
            else:
                return False

        return True


# Performance Result:
#   Coding Time: 00:10:00
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 88 ms, faster than 16.05%
#   Memory Usage: 14 MB, less than 36.25%
