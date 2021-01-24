SELECT
    a.player_id,
    a.device_id
FROM
    Activity a
INNER JOIN (
    SELECT
        player_id,
        MIN(event_date) AS first_date
    FROM
        Activity
    GROUP BY
        player_id
) b
ON (a.player_id = b.player_id AND a.event_date = b.first_date);


-- Performance Result:
--   Coding Time: 00:04:51
--   Runtime: 459 ms, faster than 76.60%
--   Memory Usage: 0B, less than 100.00%
