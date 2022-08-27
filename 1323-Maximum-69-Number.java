import java.util.ArrayList;
import java.lang.Math;

class Solution {
    public int maximum69Number (int num) {
        ArrayList<Integer> digits = new ArrayList<>();
        while (num > 0) {
            int digit = num % 10;
            digits.add(digit);
            num /= 10;
        }

        boolean isChanged = false;
        int res = 0;
        for (int i = digits.size() - 1; i >= 0; i--) {
            int digit = digits.get(i);
            if (digit == 6 && !isChanged) {
                res += 9 * (int)Math.pow(10.0, (double)i);
                isChanged = true;
            } else {
                res += digit * (int)Math.pow(10.0, (double)i);
            }
        }

        return res;
    }
}

// Performance Result:
//   Coding Time: 00:09:06
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 86.18%
//   Memory Usage: 41.6 MB, less than 20.03%
