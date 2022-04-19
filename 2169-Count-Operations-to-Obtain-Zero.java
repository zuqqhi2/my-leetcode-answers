class Solution {
    public int countOperations(int num1, int num2) {
        int res = 0;
        while (num1 > 0 && num2 > 0) {
            if (num1 >= num2) num1 -= num2;
            else num2 -= num1;
            res += 1;
        }

        return res;
    }
}



// Performance Result:
//   Coding Time: 00:03:06
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 70.79%
//   Memory Usage: 39.2 MB, less than 90.48%
