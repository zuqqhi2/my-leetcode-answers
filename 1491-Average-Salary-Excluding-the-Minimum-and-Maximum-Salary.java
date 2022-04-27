import java.util.Arrays;

class Solution {
    public double average(int[] salary) {
        Arrays.sort(salary);

        double res = 0.0;
        for (int i = 1; i < salary.length - 1; i++) {
            res += salary[i];
        }
        return res / (salary.length - 2);
    }
}

// Performance Result:
//   Coding Time: 00:02:14
//   Time Complexity: O(N log N)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 35.81%
//   Memory Usage: 41.6 MB, less than 55.44%
