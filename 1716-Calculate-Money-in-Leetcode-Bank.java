class Solution {
    public int totalMoney(int n) {
        int res = 0;
        for (int i = 0; i < n / 7 + 1; i++) {
            for (int j = 0; j < 7; j++) {
                if (i * 7 + j + 1 <= n)
                    res += i + j + 1;
            }
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:06:22
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 63.61%
//   Memory Usage: 39 MB, less than 91.44%
