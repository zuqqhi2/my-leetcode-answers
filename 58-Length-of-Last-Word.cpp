class Solution {
public:
    /**
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    int lengthOfLastWord(string s) {
        // If there is no last word, return 0
        if (s == " " || s.size() == 0) { return 0; }

        int length = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (length > 0 && s[i] == ' ') { break;       }
            else if (s[i] != ' ')          { length += 1; }
        }

        return length;
    }
};

// Sample Testcase:
//   Input:
//     "Hello World"
//   Output:
//     5

// Performance Result:
//   Coding Time: 00:07:12
//   Runtime: 4 ms, faster than 96.47% of C++ online submissions for Length of Last Word.
//   Memory Usage: 8.7 MB, less than 83.86% of C++ online submissions for Length of Last Word.
