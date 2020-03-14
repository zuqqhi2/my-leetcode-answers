class Node:
    def __init__(self, val: int, prev: 'List[Node]' = []):
        self.val = val
        self.prev = prev


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: 'List[List[int]]') -> bool:
        """
        :param int numCourses: ?
        :param List[List[int]] prerequisites: ?
        :rtype: bool
        :return: ?
        """
        # Corner cases
        if numCourses == 0:
            return True
        if prerequisites is None:
            return True
        if len(prerequisites) == 0:
            return True

        # Generate directed graph
        nodes = {i: Node(i) for i in range(numCourses)}
        for i in range(len(prerequisites)):
            nodes[prerequisites[i][0]].prev.append(nodes[prerequisites[i][1]])

        # Find a loop
        # if there is no loop, all courses can be finished
        for i in range(numCourses):
            opened = [nodes[i]]
            visited = {i: False for i in range(numCourses)}
            while len(opened) > 0:
                cur_node = opened.pop(0)
                visited[cur_node.val] = True

                for prev_node in cur_node.prev:
                    # Loop check
                    if i == prev_node.val:
                        return False
                    # Add new nodes to the open list
                    if not visited[prev_node.val]:
                        opened.insert(0, prev_node)

        return True


# Sample test case:
#   Input:
#       numCourses = 2, prerequisites = [[1,0],[0,1]]
#   Output:
#       False

# Performance Result:
#   Coding Time: 00:47:09
#   Time Complexity: O(N^2)
#   Space Complexity: O(N^2)
#   Runtime: 1332 ms, faster than 5.00% of Python3
#       online submissions for Course Schedule.
#   Memory Usage: 14.5 MB, less than 65.31% of Python3
#       online submissions for Course Schedule.
