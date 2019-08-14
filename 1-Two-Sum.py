from bisect import bisect_left


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find 2 values' idx which sum of them equals target using Hash Table.
        Complexity is n
        """

        # Create dictionary which key is number and value is index
        # for searching index of target - value1
        num_dict = {}
        for idx, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(idx)
            else:
                num_dict[num] = [idx]

        # Pick up 1 and find index of target - 1's number using Hash Table
        for num1 in num_dict.keys():
            ans_num = target - num1
            if ans_num in num_dict:
                # If it chooses same number twise and
                # there are 2 indexes in the dictionary, return those
                if num1 == ans_num and len(num_dict[ans_num]) >= 2:
                    return num_dict[ans_num][0:2]
                elif num1 != ans_num:
                    return [num_dict[num1][0], num_dict[ans_num][0]]

        # No answer combination
        return None

# Sample Testcase:
#   Input:
#     [2,7,11,15]
#     9
#   Output:
#     [0,1]

# Performance Result:
#   Runtime: 40 ms, faster than 86.83% of Python3 online submissions for Two Sum.
#   Memory Usage: 15.6 MB, less than 5.08% of Python3 online submissions for Two Sum.
