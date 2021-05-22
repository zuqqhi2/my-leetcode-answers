class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ori_arr = arr[:]
        is_second = False
        cur_pos = 0
        for i in range(len(arr)):
            arr[i] = ori_arr[cur_pos]
            if ori_arr[cur_pos] == 0 and not is_second:
                is_second = True
            else:
                is_second = False
                cur_pos += 1

        return None


# Performance Result:
#   Coding Time: 00:05:50
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 68 ms, faster than 80.83%
#   Memory Usage: 15 MB, less than 9.24%
