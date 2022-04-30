import java.util.HashMap;
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashMap<Integer,ArrayList<Integer>> next = new HashMap<>();
        for (int i = 0; i < edges.length; i++) {
            next.putIfAbsent(edges[i][0], new ArrayList<Integer>());
            next.putIfAbsent(edges[i][1], new ArrayList<Integer>());

            ArrayList<Integer> nextNodes = next.get(edges[i][0]);
            nextNodes.add(edges[i][1]);

            nextNodes = next.get(edges[i][1]);
            nextNodes.add(edges[i][0]);
        }

        ArrayList<Integer> opened = new ArrayList<>();
        HashSet<Integer> visited = new HashSet<>();
        opened.add(source);
        visited.add(source);
        while (opened.size() > 0) {
            int curNode = opened.get(0);
            if (curNode == destination) return true;

            visited.add(curNode);
            opened.remove(0);

            ArrayList<Integer> nextNodes = next.get(curNode);
            for (int i = 0; i < nextNodes.size(); i++) {
                if (visited.contains(nextNodes.get(i))) continue;
                opened.add(nextNodes.get(i));
            }
        }

        return false;
    }
}

// Performance Result:
//   Coding Time: 00:12:22
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 198 ms, faster than 43.29%
//   Memory Usage: 232.7 MB, less than 20.25%
