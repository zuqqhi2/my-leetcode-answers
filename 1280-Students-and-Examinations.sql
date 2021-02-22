# Write your MySQL query statement below
SELECT
    st.student_id,
    st.student_name,
    su.subject_name,
    SUM(IF(ex.subject_name IS NOT NULL, 1, 0)) AS attended_exams
FROM
    Students st
CROSS JOIN
    Subjects su
LEFT OUTER JOIN
    Examinations ex
ON (st.student_id = ex.student_id AND su.subject_name = ex.subject_name)
GROUP BY
    st.student_id,
    st.student_name,
    su.subject_name
ORDER BY
    st.student_id,
    su.subject_name;

-- Performance Result:
--   Coding Time: 00:12:32
--   Runtime: 704 ms, faster than 45.69%
--   Memory Usage: 0B, less than 100.00%
