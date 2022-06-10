/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public boolean isUnivalTree(TreeNode root) {
        ArrayList<TreeNode> opened = new ArrayList<>();
        HashSet<Integer> values = new HashSet<>();

        opened.add(root);
        values.add(root.val);
        while (opened.size() > 0) {
            TreeNode curNode = opened.get(0);
            opened.remove(0);

            if (!values.contains(curNode.val)) {
                return false;
            }

            if (curNode.left != null) opened.add(curNode.left);
            if (curNode.right != null) opened.add(curNode.right);
        }

        return true;
    }
}


// Performance Result:
//   Coding Time: 00:04:04
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 16.03%
//   Memory Usage: 42.2 MB, less than 15.56%
