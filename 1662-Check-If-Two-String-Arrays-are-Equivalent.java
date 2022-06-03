import java.util.StringJoiner;

class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringJoiner sj = new StringJoiner("");
        for (String s : word1) { sj.add(s); }
        String word1Res = sj.toString();

        sj = new StringJoiner("");
        for (String s : word2) { sj.add(s); }
        String word2Res = sj.toString();

        if (word1Res.equals(word2Res))
            return true;
        else
            return false;
    }
}


// Performance Result:
//   Coding Time: 00:04:29
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 90.25%
//   Memory Usage: 40.2 MB, less than 89.90%
