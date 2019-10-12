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
var maxDepth = function (root) {
    if (root === null) { return 0 }

    var stuck = [[root.left, 1], [root.right, 1]]
    var maxCount = 1
    while (stuck.length >= 1) {
        var curNode = stuck.shift()
        if (curNode[0] !== null) {
            var curCount = curNode[1] + 1
            if (curNode[0].left !== undefined) { stuck.unshift([curNode[0].left, curCount]) }
            if (curNode[0].right !== undefined) { stuck.unshift([curNode[0].right, curCount]) }

            if (curCount > maxCount) { maxCount = curCount }
        }
    }

    return maxCount;
};

// Debug Code
var t = new TreeNode(1)
console.log(maxDepth(t)) // => 1

// Sample Testcase:
//   Input:
//     [3,9,20,null,null,15,7]
//   Output:
//     3

// Performance Result:
//   Coding Time: 00:17:23
//   Runtime: 68 ms, faster than 27.71% of JavaScript online submissions for Maximum Depth of Binary Tree.
//   Memory Usage: 37.3 MB, less than 28.13% of JavaScript online submissions for Maximum Depth of Binary Tree.