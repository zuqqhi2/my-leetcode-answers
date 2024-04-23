impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        let mut idx1 = 0;
        let mut idx2 = 0;
        while idx1 < nums1.len() && idx2 < nums2.len() {
            if nums1[idx1][0] == nums2[idx2][0] {
                res.push(vec![nums1[idx1][0], nums1[idx1][1] + nums2[idx2][1]]);
                idx1 += 1;
                idx2 += 1;
            } else if nums1[idx1][0] > nums2[idx2][0] {
                res.push(vec![nums2[idx2][0], nums2[idx2][1]]);
                idx2 += 1;
            } else {
                res.push(vec![nums1[idx1][0], nums1[idx1][1]]);
                idx1 += 1;
            }
        }

        while idx1 < nums1.len() {
            res.push(vec![nums1[idx1][0], nums1[idx1][1]]);
            idx1 += 1;
        }
        while idx2 < nums2.len() {
            res.push(vec![nums2[idx2][0], nums2[idx2][1]]);
            idx2 += 1;
        }

        return res;
    }
}

// Performance Result:
//   Coding Time: 00:16:39
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 100.00%
//   Memory Usage: 2.21 MB, less than 28.57%
