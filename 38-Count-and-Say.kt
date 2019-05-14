class Solution {
    /**
     * Time Complexity:  O(nm)
     * Space Complexity: O(1)
     */
    fun countAndSay(n: Int): String {
        // Generate count-and-say sequence
        var prevSeq = "1"
        var curSeq = ""
        for (i in 2..n) {
            var prevNum = prevSeq.take(1).single()
            prevSeq = prevSeq.drop(1)
            var count = 1
            // Count number of same digit in a row
            // and generate sub sequences which concatenate count and its digit
            // ex) 11122 => 31, 22
            prevSeq.forEach {
                if (it == prevNum) {
                    count += 1
                } else {
                    curSeq = curSeq.plus(count.toString().plus(prevNum))
                    prevNum = it
                    count = 1
                }
            }
            curSeq = curSeq.plus(count.toString().plus(prevNum))

            // Save current sequence as prev and clear current sequence
            prevSeq = curSeq
            curSeq = ""
        }

        return prevSeq
    }
}

// Sample Testcase:
//   Input:
//     4
//   Output:
//     1211

// Performance Result:
//   Coding Time: 01:28:09
//   Runtime: 184 ms, faster than 32.81% of Kotlin online submissions for Count and Say.
//   Memory Usage: 35.7 MB, less than 100.00% of Kotlin online submissions for Count and Say.
