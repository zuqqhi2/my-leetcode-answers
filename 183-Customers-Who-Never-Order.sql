# Write your MySQL query statement below
SELECT c.Name AS Customers
FROM Customers c
LEFT OUTER JOIN Orders o
ON (c.Id = o.CustomerId)
WHERE o.Id is NULL
GROUP BY c.Id, c.Name;

-- Performance Result:
--   Coding Time: 00:03:12
--   Runtime: 432 ms, faster than 62.19%
--   Memory Usage: 0B, less than 100.00%
