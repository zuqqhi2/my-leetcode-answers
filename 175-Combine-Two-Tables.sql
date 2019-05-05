# Write your MySQL query statement below

SELECT
    allData.FirstName,
    allData.LastName,
    allData.City,
    allData.State
FROM (
    SELECT
        p1.PersonId,
        MIN(a1.AddressId) AS minAdrId
    FROM
        Person p1
    INNER JOIN
        Address a1
    ON
        p1.PersonId = a1.PersonId
    GROUP BY
        p1.PersonId
) minAddress
RIGHT OUTER JOIN (
    SELECT
        p2.PersonId,
        a2.AddressId,
        p2.FirstName,
        p2.LastName,
        a2.City,
        a2.State
    FROM
        Person p2
    LEFT OUTER JOIN
        Address a2
    ON
        p2.PersonId = a2.PersonId
) allData
ON
    allData.PersonId = minAddress.PersonId
    AND allData.AddressId = minAddress.minAdrId
ORDER BY
    allData.FirstName ASC,
    allData.LastName ASC;

-- Sample Testcase:
--   Input:
--     {"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}
--   Output:
--     {"headers":["FirstName","LastName","City","State"],"values":[["Allen","Wang",null,null]]}

-- Performance Result:
--   Runtime: 221 ms, faster than 50.43% of MySQL online submissions for Combine Two Tables.
--   Memory Usage: N/A
