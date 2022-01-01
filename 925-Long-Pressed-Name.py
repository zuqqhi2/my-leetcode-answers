class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx = 0
        typed_idx = 0
        while name_idx <= len(name) and typed_idx < len(typed):
            if name_idx < len(name) and name[name_idx] == typed[typed_idx]:
                name_idx += 1
                typed_idx += 1
            elif name_idx > 0 and name[name_idx - 1] == typed[typed_idx]:
                typed_idx += 1
            else:
                return False

        return False if name_idx < len(name) or typed_idx < len(typed) else True


# Performance Result:
#   Coding Time: 00:16:54
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 66.22%
#   Memory Usage: 14.2 MB, less than 84.83%
