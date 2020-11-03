-- Write your MySQL query statement below
SELECT
    a.id
FROM
    Weather a
INNER JOIN (
    SELECT
        recordDate,
        MAX(temperature) as maxTemp
    FROM
        Weather
    GROUP BY
        recordDate
) b
ON DATE_SUB(a.recordDate, INTERVAL 1 DAY) = b.recordDate
WHERE
    a.temperature > b.maxTemp
ORDER BY
    a.id;

-- Performance Result:
--   Coding Time: 00:11:40
--   Runtime: 319 ms, faster than 90.85%
--   Memory Usage: 0B, less than 100.00%
