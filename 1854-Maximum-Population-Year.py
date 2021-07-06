class Solution:
    from collections import Counter

    def maximumPopulation(self, logs: List[List[int]]) -> int:

        min_year = float('inf')
        max_year = float('-inf')
        max_pop = float('-inf')
        output = None
        delta_map = Counter()

        for person in logs:
            # unpack tuple
            (birth, death) = person

            # update the delta map for this person's birth and death
            delta_map[birth] += 1
            delta_map[death] -= 1

            # update min and max years
            min_year = min(min_year, birth)
            max_year = max(max_year, death)

        alive_ct = 0
        # now find the year with the most people alive
        for year in range(min_year, max_year):

            alive_ct += delta_map[year]

            if alive_ct > max_pop:
                output = year
                max_pop = alive_ct

        return output


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 84.60%
#   Memory Usage: 14.3 MB, less than 66.07%
