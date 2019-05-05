class Solution {

    /**
     * Check a given value is palindrome or not
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     *
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        // If minus value is given, it's always like '-123' so '-' causes false
        if ($x < 0) { return false; }

        // Convert integer to char array
        $int_char_ary = str_split(strval($x));

        // Prepare variables to avoid calculation many times in next loop
        $stack = [];
        $char_num = count($int_char_ary);
        $is_odd = count($int_char_ary) %2 == 1 ? true : false;
        $center_idx = floor(count($int_char_ary) / 2);

        // Scan each interger character
        for ($i = 0; $i < $char_num; $i++) {
            // Skip center number because any number is OK
            if ($is_odd && $i == $center_idx) {
                continue;
            // After center number,
            // check numbers after center are reverse order of numbers before center
            } else if ($i >= $center_idx) {
                $char = array_pop($stack);
                // if there is not appropriate value, return false immediately
                if ($char != $int_char_ary[$i]) { return false; }
            // Before center, just push number to stack
            } else {
                array_push($stack, $int_char_ary[$i]);
            }
        }

        return true;
    }
}

// Sample Testcase:
//   Input:
//     121
//   Output:
//     true

// Performance Result:
//   Runtime: 88 ms, faster than 49.67% of PHP online submissions for Palindrome Number.
//   Memory Usage: 14.8 MB, less than 35.29% of PHP online submissions for Palindrome Number.
