class Solution {
    func charAt(_ str: String, _ idx: Int) -> Character {
        return str[str.index(str.startIndex, offsetBy: idx)]
    }

    /**
     * Time Complexity: O(nm)
     * Space Complexity: O(1)
     */
    func strStr(_ haystack: String, _ needle: String) -> Int {
        // If needle is empty string, return 0
        if needle == "" { return 0 }

        // If haystack is empty string, it shouldn't have needle inside
        if haystack == "" { return -1 }

        // If haystack and needle are completely same, return 0 immediately
        if haystack == needle { return 0 }

        // Scan all chars of haystack
        for cur_idx in 0...haystack.count {
            //
            for needle_idx in (0..<needle.count).reversed() {
                // If needle length is more than haystack remaining string, return -1
                if cur_idx + needle_idx >= haystack.count { return -1 }
                // Even if there is only 1 char diff, go to next
                if charAt(haystack, cur_idx + needle_idx) != charAt(needle, needle_idx) {
                    break
                // Found needle in haystack with cur_idx
                } else if needle_idx == 0 {
                    return cur_idx
                }
            }
        }

        return -1
    }
}

// Sample Testcase:
//   Input:
//     haystack = "hello"
//     needle = "ll"
//   Output:
//     2

// Performance Result:
//   Coding Time: 01:07:13 (Learning swift took time)
//   Runtime: 24 ms, faster than 30.40% of Swift online submissions for Implement strStr().
//   Memory Usage: 20.8 MB, less than 9.09% of Swift online submissions for Implement strStr().
