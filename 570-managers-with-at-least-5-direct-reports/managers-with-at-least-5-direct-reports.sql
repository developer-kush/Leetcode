# Write your MySQL query statement below

SELECT s.name 
FROM Employee as f INNER JOIN Employee as s ON f.managerId = s.id
GROUP BY s.id
HAVING COUNT(DISTINCT f.id) >= 5;