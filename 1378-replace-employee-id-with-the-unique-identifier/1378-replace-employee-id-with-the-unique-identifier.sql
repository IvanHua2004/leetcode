# Write your MySQL query statement below
SELECT UNI.unique_id, E.name
FROM Employees AS E
LEFT JOIN EmployeeUNI AS UNI ON E.id = UNI.id
