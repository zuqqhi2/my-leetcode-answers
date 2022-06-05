import java.util.HashSet;

class Solution {
    public boolean checkIfExist(int[] arr) {
        HashSet<Integer> values = new HashSet<>();
        int numZero = 0;
        for (int i : arr) {
            if (i == 0) {
                numZero += 1;
                if (numZero >= 2) return true;
            }
            values.add(i);
        }

        HashSet<Integer> values2 = new HashSet<>();
        for (int i : values) {
            if (values2.contains(i) || values2.contains(i * 2)) return true;
            values2.add(i);
            values2.add(i * 2);
        }
        return false;
    }
}


// Performance Result:
//   Coding Time: 00:12:05
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 6 ms, faster than 13.19%
//   Memory Usage: 44.9 MB, less than 5.58%
