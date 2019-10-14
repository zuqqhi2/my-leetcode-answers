/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}


/**
* @param {TreeNode} root
* @return {number}
*/
var minDepth = function (root) {
    if (root === null || root === undefined) { return 0; }

    var minDepth = 1000000;
    var stuck = [[root, 1]];
    while (stuck.length >= 1) {
        var curElem = stuck.shift();
        var curNode = curElem[0];
        var curDepth = curElem[1];
        if (curNode.left === null && curNode.right === null) {
            if (curDepth < minDepth) { minDepth = curDepth; }
        }

        if (curNode.left !== null) {
            stuck.unshift([curNode.left, curDepth + 1]);
        }

        if (curNode.right !== null) {
            stuck.unshift([curNode.right, curDepth + 1]);
        }
    }

    return minDepth;
};

var n = new TreeNode(1);
console.log(minDepth(n));

// Sample Testcase:
//   Input:
//     [3,9,20,null,null,15,7]
//   Output:
//     2

// Performance Result:
//   Coding Time: 00:10:00
//   Time Complexity: O(n)
//   Space Complexity: O(n)
//   Runtime: 68 ms, faster than 31.52% of JavaScript
//      online submissions for Minimum Depth of Binary Tree.
//   Memory Usage: 37.4 MB, less than 40.00% of JavaScript
//      online submissions for Minimum Depth of Binary Tree.
