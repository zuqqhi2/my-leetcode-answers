SELECT
    MIN(ABS(a.x - b.x)) AS shortest
FROM
    point a
CROSS JOIN
    point b
WHERE
    a.x != b.x;

-- Performance Result:
--   Coding Time: 00:01:55
--   Runtime: 228 ms, faster than 54.91%
--   Memory Usage: 0B, less than 100.00%
