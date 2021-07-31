SELECT a.employee_id
FROM Employees a
INNER JOIN Employees b ON a.manager_id = b.employee_id
INNER JOIN Employees c ON b.manager_id = c.employee_id
INNER JOIN Employees d ON c.manager_id = d.employee_id
WHERE a.employee_id != 1 AND (b.employee_id = 1 OR c.employee_id = 1 OR d.employee_id = 1);

-- Performance Result:
--   Coding Time: 00:07:45
--   Runtime: 204 ms, faster than 56.80%
--   Memory Usage: 0B, less than 100.00%
