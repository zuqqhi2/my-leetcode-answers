SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM
    DailySales
GROUP BY
    date_id,
    make_name;

-- Performance Result:
--   Coding Time: 00:02:19
--   Runtime: 473 ms, faster than 51.80%
--   Memory Usage: 0B, less than 100.00%
