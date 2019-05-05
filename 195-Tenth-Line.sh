#!/bin/bash

# Read from the file file.txt and output the tenth line to stdout.
if [ "$(cat file.txt | wc -l)" -ge 10 ]; then
    head -10 file.txt | tail -1
fi

# Sample Testcase:
#   Input:
#     Line 1
#     ...
#     Line 10
#   Output:
#     Line 10

# Performance Result:
#   Runtime: 4 ms, faster than 100.00% of Bash online submissions for Tenth Line.
#   Memory Usage: 3.7 MB, less than 44.92% of Bash online submissions for Tenth Line.
