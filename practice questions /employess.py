# Write your MySQL query statement below
'''
SELECT Employee.name AS Employee
FROM Employee 
JOIN Employee manager ON Employee.managerId = manager.id
WHERE Employee.salary > manager.salary;
'''
