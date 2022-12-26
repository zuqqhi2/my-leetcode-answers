impl Solution {
    pub fn apply_operations(nums: Vec<i32>) -> Vec<i32> {
        let mut v: Vec<i32> = Vec::new();
        let mut is_skip_next = false;
        let mut num_zero = 0;

        for i in 0..nums.len()-1 {
            if is_skip_next {
                is_skip_next = false;
                continue;
            }

            if nums[i] == 0 {
                num_zero += 1;
            } else if nums[i] == nums[i + 1] {
                v.push(nums[i] * 2);
                is_skip_next = true;
                num_zero += 1;
            } else {
                v.push(nums[i]);
            }
        }

        if nums[nums.len() - 1] == 0 {
            num_zero += 1;
        } else if !is_skip_next {
            v.push(nums[nums.len() - 1]);
        }

        for i in 0..num_zero {
            v.push(0);
        }

        return v;
    }
}

// Performance Result:
//   Coding Time: 00:18:09
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 77.78%
//   Memory Usage: 2.2 MB, less than 51.39%
