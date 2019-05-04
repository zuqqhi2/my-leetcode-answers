class Solution {
     /**
     * Return a reversed given integer(reversing as string)
     *
     * @args x reverse target integer
     * @return return reversed integer with keeping sign
     */
    fun reverse(x: Int): Int {
        // Convert integer to string
        val xStr:String = Integer.toString(x)

        // Reverse digits without minus sign
        val reversedStr:String = if (xStr.first() == '-') {
            "-".plus(xStr.drop(1).reversed())
        } else {
            xStr.reversed()
        }

        // Return reversed integer after converting
        // If reversed integer exceeds the interger limit, return 0
        try {
            return Integer.parseInt(reversedStr)
        } catch(e: NumberFormatException) {
            return 0
        }
    }
}

// Sample Testcase:
//   Input:
//     -123
//   Output:
//     -321

// Performance Result:
//   Runtime: 168 ms, faster than 53.15% of Kotlin online submissions for Reverse Integer.
//   Memory Usage: 35.1 MB, less than 15.38% of Kotlin online submissions for Reverse Integer.
