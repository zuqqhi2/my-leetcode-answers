class Solution {
    /**
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public int[] plusOne(int[] digits) {
        // Return 1 element array for only when given array is empty
        if (digits.length == 0) {
            int[] result = {1};
            return result;
        }

        // Plus one with carry
        int idx = digits.length - 1;
        while (idx >= 0) {
            digits[idx] = (digits[idx] + 1) % 10;
            idx -= 1;
            if (digits[idx + 1] != 0) { break; }
        }

        // When carry happens at top digit, expand the array and insert 1 to the top
        if (idx < 0 && digits[idx + 1] == 0) {
            int[] result = new int[digits.length + 1];
            System.arraycopy(digits, 0, result, 1, digits.length);
            result[0] = 1;
            return result;
        } else {
            return digits;
        }
    }
}

// Sample Testcase:
//   Input:
//     [1,2,3]
//   Output:
//     [1,2,4]

// Performance Result:
//   Coding Time: 00:15:07
//   Runtime: 0 ms, faster than 100.00% of Java online submissions for Plus One.
//   Memory Usage: 34.4 MB, less than 100.00% of Java online submissions for Plus One.
