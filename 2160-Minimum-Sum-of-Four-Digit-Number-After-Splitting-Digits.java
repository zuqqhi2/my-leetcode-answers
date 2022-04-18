import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int minimumSum(int num) {
        ArrayList<Integer> digits = new ArrayList<Integer>();
        while (num > 0) {
            digits.add(num % 10);
            num = num / 10;
        }

        Collections.sort(digits);

        return ( digits.get(0) * 10 + digits.get(3)) + (digits.get(1) * 10 + digits.get(2));
    }
}


// Performance Result:
//   Coding Time: 00:10:56
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 79.57%
//   Memory Usage: 38.9 MB, less than 96.75%
