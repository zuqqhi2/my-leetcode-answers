class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_num_repeat = 0
        length = len(word)

        for cur_pos in range(len(sequence)):
            num_repeat = 0
            while sequence[cur_pos:cur_pos + length] == word:
                cur_pos += length
                num_repeat += 1

            max_num_repeat = max(max_num_repeat, num_repeat)

        return max_num_repeat


# Performance Result:
#   Coding Time: 00:03:58
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 58.05%
#   Memory Usage: 14.1 MB, less than 70.79%
