SELECT
    x.customer_id,
    x.product_id,
    x.product_name
FROM (
    SELECT
        o2.customer_id,
        o2.product_id,
        p2.product_name,
        b.most_frequent_num_order,
        COUNT(*) AS num_order
    FROM
        Orders o2
    INNER JOIN Products p2 ON (o2.product_id = p2.product_id)
    LEFT OUTER JOIN (
        SELECT
            a.customer_id,
            MAX(a.num_order) AS most_frequent_num_order
        FROM (
            SELECT
                o.customer_id,
                o.product_id,
                p.product_name,
                COUNT(*) AS num_order
            FROM
                Orders o
                INNER JOIN Products p ON (o.product_id = p.product_id)
            GROUP BY
                o.customer_id,
                o.product_id
        ) a
        GROUP BY
            a.customer_id
    ) b ON (o2.customer_id = b.customer_id)
    GROUP BY
        o2.customer_id,
        o2.product_id
    HAVING
        num_order = most_frequent_num_order
) x;


-- Performance Result:
--   Coding Time: 00:31:10
--   Runtime: 1792 ms, faster than 55.91%
--   Memory Usage: 0B, less than 100.00%
