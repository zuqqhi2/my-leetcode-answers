import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        Map<Integer,Integer> numCounts = new HashMap<Integer,Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numCounts.containsKey(nums[i]))
                numCounts.put(nums[i], numCounts.get(nums[i]) + 1);
            else
                numCounts.put(nums[i], 1);
        }
        return numCounts.containsKey(target) && numCounts.get(target) > nums.length / 2 ? true : false;
    }
}


// Performance Result:
//   Coding Time: 00:07:51
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 3 ms, faster than 5.40%
//   Memory Usage: 43.2 MB, less than 8.74%
