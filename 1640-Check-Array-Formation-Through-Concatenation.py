class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def traverse(arr: List[int], pieces: List[List[int]]) -> bool:
            if len(arr) == 0:
                return True

            result = False
            for i in range(len(pieces)):
                is_same = True
                for j in range(len(pieces[i])):
                    if j >= len(arr) or arr[j] != pieces[i][j]:
                        is_same = False
                        break

                if is_same:
                    new_pieces = pieces[:]
                    del new_pieces[i]
                    result = traverse(arr[len(pieces[i]):], new_pieces)

            return result

        return traverse(arr, pieces)


# Performance Result:
#   Coding Time: 00:14:34
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 19.02%
#   Memory Usage: 14.4 MB, less than 35.71%
