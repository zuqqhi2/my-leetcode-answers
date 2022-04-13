import java.lang.StringBuilder;
import java.util.ArrayList;

class Solution {
    public String[] divideString(String s, int k, char fill) {
        ArrayList<String> res = new ArrayList<String>();

        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (count >= k) {
                res.add(sb.toString());
                count = 0;
                sb = new StringBuilder();
            }
            sb.append(s.charAt(i));
            count += 1;
        }

        while (sb.length() < k) {
            sb.append(fill);
        }
        res.add(sb.toString());

        return res.toArray(new String[res.size()]);
    }
}


// Performance Result:
//   Coding Time: 00:12:11
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 98.86%
//   Memory Usage: 42.2 MB, less than 90.64%
