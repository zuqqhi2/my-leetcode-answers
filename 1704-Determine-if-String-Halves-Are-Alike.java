class Solution {
    private boolean checkVowel(String s) {
        if (s.equals("a") || s.equals("e") || s.equals("i") || s.equals("o") || s.equals("u"))
            return true;
        else if (s.equals("A") || s.equals("E") || s.equals("I") || s.equals("O") || s.equals("U"))
            return true;
        else
            return false;
    }

    public boolean halvesAreAlike(String s) {
        String[] chars = s.split("");
        int pivot = chars.length / 2;

        int firstStrVowelNum = 0;
        for (int i = 0; i < pivot; i++)
            if (checkVowel(chars[i])) firstStrVowelNum += 1;

        int secondStrVowelNum = 0;
        for (int i = pivot; i < chars.length; i++)
            if (checkVowel(chars[i])) secondStrVowelNum += 1;

        if (firstStrVowelNum == secondStrVowelNum) return true;
        else return false;
    }
}


// Performance Result:
//   Coding Time: 00:06:04
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 37 ms, faster than 5.13%
//   Memory Usage: 46.7 MB, less than 5.05%
