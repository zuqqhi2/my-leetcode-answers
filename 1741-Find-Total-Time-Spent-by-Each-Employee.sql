SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM
    Employees
GROUP BY
    day, emp_id;


-- Performance Result:
--   Coding Time: 00:03:05
--   Runtime: 399 ms, faster than 89.98%
--   Memory Usage: 0B, less than 100.00%
