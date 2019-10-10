/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    // Breadth First Search
    queue = [[p, q]]
    while (queue.length > 0) {
        curElem = queue.shift();

        if (curElem[0] !== null && curElem[1] !== null) {
            // Compare children value
            if (curElem[0].val !== curElem[1].val) { return false; }

            // If both tree's left or right nodes are not null,
            // add them into queue.
            if (curElem[0].left !== null && curElem[1].left !== null) {
                queue.push([curElem[0].left, curElem[1].left])
            } else if (curElem[0].left !== null || curElem[1].left !== null) {
                return false;
            }

            if (curElem[0].right !== null && curElem[1].right !== null) {
                queue.push([curElem[0].right, curElem[1].right])
            } else if (curElem[0].right !== null || curElem[1].right !== null) {
                return false;
            }
        } else {
            if (curElem[0] !== curElem[1]) { return false; }
        }
    }

    // If it couldn't find difference during traversal, two trees are same.
    return true;
};

// Sample Testcase:
//   Input:
//     [1,2,3], [1,2,3]
//   Output:
//     true

// Performance Result:
//   Coding Time: 00:30:00
//   Runtime: 84 ms, faster than 8.94% of JavaScript online submissions for Same Tree.
//   Memory Usage: 33.9 MB, less than 60.00% of JavaScript online submissions for Same Tree.