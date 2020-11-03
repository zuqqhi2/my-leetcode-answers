-- Write your MySQL query statement below
UPDATE salary SET sex = IF(sex = 'm', 'f', 'm');

-- Performance Result:
--   Coding Time: 00:02:48
--   Time Complexity: O(N)
--   Space Complexity: O(1)
--   Runtime: 231 ms, faster than 53.26%
--   Memory Usage: 0B, less than 100.00%
