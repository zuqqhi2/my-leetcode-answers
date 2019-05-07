class Solution {
    /**
     * Time Complexity: O(mn)  m is number of elements and n is string length
     * Space Complexity: O(1)
     */
    public String longestCommonPrefix(String[] strs) {
        // If an empty array is given, no prefix
        if (strs.length == 0) { return ""; }

        // If only 1 element array is given, the element all chars are prefix
        if (strs.length == 1) { return strs[0]; }

        // Scan all elements' chars from head
        String prefix = "";
        for (int cur_char_idx = 0; cur_char_idx < strs[0].length(); cur_char_idx++) {
            // Check other element's same index char is same or not
            char cur_char = strs[0].charAt(cur_char_idx);
            for (int cur_elem_idx = 1; cur_elem_idx < strs.length; cur_elem_idx++) {
                if (strs[cur_elem_idx].length() <= cur_char_idx
                    || cur_char != strs[cur_elem_idx].charAt(cur_char_idx)) {
                    return prefix;
                }
            }
            // Concatenate char
            prefix += "" + cur_char;
        }

        return prefix;
    }
}

// Sample Testcase:
//   Input:
//     ["flower","flow","flight"]
//   Output:
//     "fl"

// Performance Result:
//   Coding Time: 00:09:44
//   Runtime: 1 ms, faster than 89.01% of Java online submissions for Longest Common Prefix.
//   Memory Usage: 35.4 MB, less than 96.81% of Java online submissions for Longest Common Prefix.
