SELECT
    s.id,
    s.name
FROM
    Students s
LEFT OUTER JOIN
    Departments d
ON (s.department_id = d.id)
WHERE
    d.id IS NULL;

-- Performance Result:
--   Coding Time: 00:02:53
--   Runtime: 713 ms, faster than 46.53%
--   Memory Usage: 0B, less than 100.00%
