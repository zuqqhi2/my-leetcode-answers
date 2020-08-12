class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate_row(rowIndex: int, prev: List[int]) -> List[int]:
            res = []
            num_elem = rowIndex + 1
            for i in range(num_elem):
                if i == 0 or i == num_elem - 1:
                    res.append(1)
                else:
                    res.append(prev[i - 1] + prev[i])

            return res

        res = []
        for i in range(rowIndex + 1):
            res = generate_row(i, res)

        return res


# Performance Result:
#   Coding Time: 00:05:51
#   Time Complexity: O(NK)
#   Space Complexity: O(K)
#   Runtime: 24 ms, faster than 95.36%
#   Memory Usage: 14 MB, less than 14.20%
