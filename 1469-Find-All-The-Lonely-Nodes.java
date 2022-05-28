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

class Solution {
    public List<Integer> getLonelyNodes(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<TreeNode> opened = new ArrayList<>();
        opened.add(root);
        while (opened.size() > 0) {
            TreeNode curNode = opened.get(0);
            opened.remove(0);

            if (curNode.left != null && curNode.right == null) {
                res.add(curNode.left.val);
            } else if (curNode.left == null && curNode.right != null) {
                res.add(curNode.right.val);
            }

            if (curNode.left != null)
                opened.add(curNode.left);
            if (curNode.right != null)
                opened.add(curNode.right);
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:07:14
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 5 ms, faster than 10.14%
//   Memory Usage: 46.5 MB, less than 54.14%
