import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] anagramMappings(int[] nums1, int[] nums2) {
        Map<Integer,Integer> idxMap = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) {
            idxMap.put(nums2[i], i);
        }

        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = idxMap.get(nums1[i]);
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:04:13
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 91.68%
//   Memory Usage: 43.3 MB, less than 5.33%
