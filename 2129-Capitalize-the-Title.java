class Solution {
    public String capitalizeTitle(String title) {
        String[] words = title.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            String resWord = words[i].toLowerCase();
            if (resWord.length() >= 3) {
                resWord = resWord.substring(0, 1).toUpperCase() + resWord.substring(1);
            }
            sb.append(resWord);
            if (i < words.length - 1) sb.append(' ');
        }

        return sb.toString();
    }
}


// Performance Result:
//   Coding Time: 00:09:56
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 5 ms, faster than 73.17%
//   Memory Usage: 43.1 MB, less than 54.22%
