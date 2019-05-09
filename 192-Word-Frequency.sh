#!/bin/bash

# Read from the file words.txt and output the word frequency list to stdout.
sed -e 's/ /\n/g' words.txt \
    | egrep -v "^$" \
    | sort \
    | uniq -c \
    | sort -r \
    | awk -F' ' '{ print $2" "$1 }'


# Sample Testcase:
#   Input:
#     the day is sunny the the
#     the sunny is is
#   Output:
#     the 4
#     is 3
#     sunny 2
#     day 1

# Performance Result:
#   Coding Time: 00:13:01
#   Runtime: 0 ms, faster than 100.00% of Bash online submissions for Word Frequency.
#   Memory Usage: 3.3 MB, less than 21.37% of Bash online submissions for Word Frequency.
