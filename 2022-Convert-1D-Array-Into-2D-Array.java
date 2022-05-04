class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if (m * n != original.length) {
            return new int[0][0];
        }

        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = original[i * n + j];
            }
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:04:40
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 7 ms, faster than 55.67%
//   Memory Usage: 121 MB, less than 15.28%
