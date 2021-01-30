# Write your MySQL query statement below
SELECT
    a.seat_id
FROM
    cinema a
LEFT OUTER JOIN
    cinema b
ON (a.seat_id + 1 = b.seat_id)
LEFT OUTER JOIN
    cinema c
ON (a.seat_id - 1 = c.seat_id)
WHERE
    (a.free = TRUE AND (b.free IS NOT NULL AND b.free = TRUE))
    OR (a.free = TRUE AND (c.free IS NOT NULL AND c.free = TRUE));


-- Performance Result:
--   Coding Time: 00:05:22
--   Runtime: 340 ms, faster than 44.74%
--   Memory Usage: 0B, less than 100.00%
