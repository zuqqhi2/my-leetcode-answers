import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int minOperations(String[] logs) {
        Deque<String> stack = new ArrayDeque<String>();
        for (int i = 0; i < logs.length; i++) {
            if (logs[i].equals("../")) {
                if (stack.size() > 0)
                    stack.pop();
            } else if (logs[i].equals("./")) {
                // skip
            } else {
                stack.push(logs[i]);
            }
        }

        return stack.size();
    }
}


// Performance Result:
//   Coding Time: 00:06:28
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 58.04%
//   Memory Usage: 42.5 MB, less than 58.45%
