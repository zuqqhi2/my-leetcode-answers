# Write your MySQL query statement below
SELECT
    x, y, z,
    IF(x + y > z AND y + z > x AND z + x > y, 'Yes', 'No') AS triangle
FROM triangle;


-- Performance Result:
--   Coding Time: 00:03:19
--   Runtime: 257 ms, faster than 37.66%
--   Memory Usage: 0B, less than 100.00%
