import java.util.HashSet;
import java.util.ArrayList;

class Solution {
    public int countPoints(String rings) {
        ArrayList<HashSet> rods = new ArrayList<HashSet>();
        for (int i = 0; i < 10; i++) {
            rods.add(new HashSet<String>());
        }

        for (int i = 0; i < rings.length() / 2; i++) {
            String color = rings.substring(i * 2, i * 2 + 1);
            Integer rodId = Integer.parseInt(rings.substring(i * 2 + 1, i * 2 + 2));
            rods.get(rodId.intValue()).add(color);
        }

        int res = 0;
        for (int i = 0; i < rods.size(); i++) {
            if (rods.get(i).contains("R") && rods.get(i).contains("G") && rods.get(i).contains("B")) {
                res += 1;
            }
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:17:01
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 55.00%
//   Memory Usage: 43 MB, less than 5.26%
