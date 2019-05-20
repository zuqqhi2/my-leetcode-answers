class Solution {

    /**
     * Time Complexity: O(m + n)
     * Space Complexity: O(m)
     *
     * @param Integer[] $nums1
     * @param Integer $m
     * @param Integer[] $nums2
     * @param Integer $n
     * @return NULL
     */
    function merge(&$nums1, $m, $nums2, $n) {
        // If nums2 is empty, no need any processing
        if ($n == 0) { return; }

        $pos1 = 0;
        $pos2 = 0;
        $buffer = array();
        // Scan both of the array
        while ($pos1 < $m + $n || $pos2 < $n) {
            // If current num1 value is bigger than other value,
            // or scanning num1 is already finished repalce value
            if ($pos1 >= $m
                || ($pos2 < $n && $nums1[$pos1] > $nums2[$pos2])
                || (count($buffer) >= 1 && $nums1[$pos1] > $buffer[0])) {

                // Keep nums1 element in buffer instead of switch
                if ($pos1 < $m) { array_push($buffer, $nums1[$pos1]); }

                // Replace current idx nums1 element to smaller value
                if (count($buffer) == 0
                    || (count($buffer) >= 1 && $pos2 < $n && $nums2[$pos2] < $buffer[0])) {

                    $nums1[$pos1] = $nums2[$pos2];
                    $pos2 += 1;
                } else if (count($buffer) >= 1) {
                    $nums1[$pos1] = array_shift($buffer);
                }
            }

            // Move to next element
            if ($pos1 < $m + $n) { $pos1 += 1; }
        }
    }
}

// Sample Testcase:
//   Input:
//     nums1 = [1,2,3,0,0,0], m = 3
//     nums2 = [2,5,6],       n = 3
//   Output:
//     [1,2,2,3,5,6]

// Performance Result:
//   Coding Time: 01:08:53 (because of too tired by work)
//   Runtime: 8 ms, faster than 100.00% of PHP online submissions for Merge Sorted Array.
//   Memory Usage: 15 MB, less than 15.69% of PHP online submissions for Merge Sorted Array.
