# Write your MySQL query statement below
SELECT
    ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*) * 100, 2) AS immediate_percentage
FROM
    Delivery
;


-- Performance Result:
--   Coding Time: 00:11:24
--   Runtime: 383 ms, faster than 67.31%
--   Memory Usage: 0B, less than 100.00%
