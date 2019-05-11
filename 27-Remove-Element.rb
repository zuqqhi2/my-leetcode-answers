# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
    if nums == nil or !nums.any?
        return 0
    else
        nums.delete(val)
        return nums.size
    end
end

# Sample Testcase:
#   Input:
#     nums = [3,2,2,3]
#     val = 3
#   Output:
#     2 (given array should be [2, 2])

# Performance Result:
#   Coding Time: 00:??:??
#   Runtime: 36 ms, faster than 97.77% of Ruby online submissions for Remove Element.
#   Memory Usage: 9.3 MB, less than 100.00% of Ruby online submissions for Remove Element.
