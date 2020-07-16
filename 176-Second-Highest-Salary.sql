SELECT (
    SELECT
        DISTINCT Salary
    FROM
        Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;


-- Performance Result:
--   Coding Time: -
--   Time Complexity: O(N)
--   Space Complexity: O(1)
--   Runtime: 211 ms, faster than 85.30%
--   Memory Usage: 0B, less than 100.00%
