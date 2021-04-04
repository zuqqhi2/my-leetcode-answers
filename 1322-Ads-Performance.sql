# Write your MySQL query statement below
SELECT
    a.ad_id,
    IF(a.num_click + a.num_view = 0, 0.0, ROUND(a.num_click / (a.num_click + a.num_view) * 100, 2)) AS ctr
FROM (
    SELECT
        ad_id,
        SUM(IF(action = 'Clicked', 1, 0)) AS num_click,
        SUM(IF(action = 'Viewed', 1, 0)) AS num_view
    FROM Ads
    GROUP BY ad_id
) a
GROUP BY
    a.ad_id
ORDER BY
    ctr DESC,
    a.ad_id ASC;


-- Performance Result:
--   Coding Time: 00:09:02
--   Runtime: 422 ms, faster than 52.43%
--   Memory Usage: 0B, less than 100.00%
