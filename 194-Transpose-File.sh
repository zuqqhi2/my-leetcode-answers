#!/bin/bash

# Read from the file file.txt and print its transposed content to stdout.
awk -F' ' '{
    num_rows += 1
    num_cols = NF
    for (j = 1; j <= num_cols; j++) {
        data[num_rows, j] = $j
    }
} END {
    for (j = 1; j <= num_cols; j++) {
        cur_row_str = data[1, j]
        for (i = 2; i <= num_rows; i++) {
            cur_row_str = cur_row_str" "data[i, j]
        }
        print cur_row_str
    }
}' file.txt

# Sample Testcase:
#   Input:
#     name age
#     alice 21
#     ryan 30
#   Output:
#     name alice ryan
#     age 21 30

# Performance Result:
#   Coding Time: 00:21:58
#   Runtime: 12 ms, faster than 91.52% of Bash online submissions for Transpose File.
#   Memory Usage: 6.7 MB, less than 8.75% of Bash online submissions for Transpose File.
