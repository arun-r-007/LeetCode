-- # Write your MySQL query statement below
DELETE p
FROM Person p
JOIN (
    SELECT email, MIN(id) AS min_id
    FROM Person
    GROUP BY email
) AS keep_records
ON p.email = keep_records.email
AND p.id != keep_records.min_id;
