-- Write your MySQL query statement below
SELECT
    DISTINCT a.Email
FROM
    Person a
INNER JOIN
    Person b
ON (a.Email = b.Email AND a.Id != b.Id);

-- Performance Result:
--   Coding Time: 00:02:00
--   Runtime: 334 ms, faster than 49.43%
--   Memory Usage: 0B, less than 100.00%
