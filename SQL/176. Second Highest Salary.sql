-- # Write your MySQL query statement below
-- SELECT MAX(salary) as SecondHighestSalary
-- FROM (
--     SELECT salary,
--            DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
--     FROM Employee
-- ) t
-- WHERE rnk = 2;
select(
select distinct salary 
from Employee 
order by salary desc
limit 1,1
) as SecondHighestSalary;