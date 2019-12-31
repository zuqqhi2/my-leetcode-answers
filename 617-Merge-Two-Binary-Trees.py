# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # In case of one of them is NULL return the other one
        if t1 is None:
            return t2
        elif t2 is None:
            return t1

        # Initiate DFS
        t_res = TreeNode(t1.val + t2.val)
        stuck = [(t1, t2, t_res)]

        # DFS
        while len(stuck) > 0:
            cur_elem = stuck.pop(0)

            if (cur_elem[0] is not None and cur_elem[0].left is not None) \
                    or (cur_elem[1] is not None and cur_elem[1].left is not None):
                new_node_val = 0
                next_t1_node = None
                next_t2_node = None
                if cur_elem[0] is not None and cur_elem[0].left is not None:
                    new_node_val += cur_elem[0].left.val
                    next_t1_node = cur_elem[0].left
                if cur_elem[1] is not None and cur_elem[1].left is not None:
                    new_node_val += cur_elem[1].left.val
                    next_t2_node = cur_elem[1].left
                new_node = TreeNode(new_node_val)
                cur_elem[2].left = new_node

                stuck.insert(0, (next_t1_node, next_t2_node, new_node))

            if (cur_elem[0] is not None and cur_elem[0].right is not None) \
                    or (cur_elem[1] is not None and cur_elem[1].right is not None):
                new_node_val = 0
                next_t1_node = None
                next_t2_node = None
                if cur_elem[0] is not None and cur_elem[0].right is not None:
                    new_node_val += cur_elem[0].right.val
                    next_t1_node = cur_elem[0].right
                if cur_elem[1] is not None and cur_elem[1].right is not None:
                    new_node_val += cur_elem[1].right.val
                    next_t2_node = cur_elem[1].right
                new_node = TreeNode(new_node_val)
                cur_elem[2].right = new_node

                stuck.insert(0, (next_t1_node, next_t2_node, new_node))

        return t_res


# Sample test case:
#   Input:
#       -
#   Output:
#       -

# Performance Result:
#   Coding Time: 00:28:47
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 96 ms, faster than 18.89% of Python3
#       online submissions for Merge Two Binary Trees.
#   Memory Usage: 13 MB, less than 100.00% of Python3
#       online submissions for Merge Two Binary Trees.
