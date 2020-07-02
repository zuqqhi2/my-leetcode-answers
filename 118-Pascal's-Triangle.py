class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            num_cols = i + 1
            cur_res = []
            for j in range(num_cols):
                if j == 0 or j == num_cols - 1:
                    cur_res.append(1)
                else:
                    cur_res.append(result[-1][j - 1] + result[-1][j])
            result.append(cur_res)

        return result


# Performance Result:
#   Coding Time: 00:05:29
#   Time Complexity: O(N^2)
#   Space Complexity: O(N^2)
#   Runtime: 28 ms, faster than 77.37%
#   Memory Usage: 13.6 MB, less than 99.71%
