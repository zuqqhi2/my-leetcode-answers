SELECT a.Name AS Employee FROM Employee a JOIN Employee b ON a.ManagerId = b.Id WHERE a.Salary > b.Salary;

-- Performance Result:
--   Coding Time: 00:03:11
--   Time Complexity: -
--   Space Complexity: -
--   Runtime: 498 ms, faster than 41.11%
--   Memory Usage: 0B, less than 100.00%
