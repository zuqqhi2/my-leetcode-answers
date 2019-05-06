#!/bin/bash

# Read from the file file.txt and output all valid phone numbers to stdout.
while read LINE
do
  echo "${LINE}" | egrep "^([0-9]{3}-|\([0-9]{3}\)\s)[0-9]{3}-[0-9]{4}$"
done < file.txt

# Sample Testcase:
#   Input:
#     987-123-4567
#     123 456 7890
#     (123) 456-7890
#   Output:
#     987-123-4567
#     (123) 456-7890

# Performance Result:
#   Runtime: 136 ms, faster than 14.44% of Bash online submissions for Valid Phone Numbers.
#   Memory Usage: 3.1 MB, less than 80.95% of Bash online submissions for Valid Phone Numbers.
