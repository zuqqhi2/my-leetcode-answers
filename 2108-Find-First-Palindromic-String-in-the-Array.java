class Solution {
    public String firstPalindrome(String[] words) {
        for (int i = 0; i < words.length; i++) {
            boolean isPalindromic = true;

            int endIdx = words[i].length() / 2;
            for (int j = 0; j < endIdx; j++) {
                if (words[i].charAt(j) != words[i].charAt(words[i].length() - 1 - j)) {
                    isPalindromic = false;
                    break;
                }
            }

            if (isPalindromic)
                return words[i];
        }

        return "";
    }
}


// Performance Result:
//   Coding Time: 00:14:03
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 3 ms, faster than 83.42%
//   Memory Usage: 51.2 MB, less than 38.87%
