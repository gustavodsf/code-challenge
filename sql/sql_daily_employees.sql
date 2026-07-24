/*
CoderPad provides a basic SQL sandbox with the following schema.
You can also use commands like `show tables` and `desc employees`

employees                                         projects
+---------------+---------+                       +---------------+---------+
| id            | int     |<----------+      +--->| id            | int     |
| first_name    | varchar |           |      |    | title         | varchar |
| last_name     | varchar |           |      |    | start_date    | date    |
| salary        | int     |           |      |    | end_date      | date    |
| department_id | int     |-----+     |      |    | budget        | int     |
+---------------+---------+     |     |      |    +---------------+---------+
                                |     |      |    
                                |     |      |    
                                |     |      |    
                                |     |      |    
departments                     |     |      |    employees_projects
+---------------+---------+     |     |      |    +---------------+---------+
| id            | int     |<----+     |      +----| project_id    | int     |
| name          | varchar |           +-----------| employee_id   | int     |
+---------------+---------+                       +---------------+---------+
*/

SELECT e.first_name, e.last_name, e.salary,
  d.name as department_name
FROM employees   AS e
JOIN departments AS d ON e.department_id = d.id;

SELECT id, first_name, last_name, salary, department_id FROM employees ORDER BY salary DESC;


SELECT  e2.salary FROM employees e2 WHERE e2.salary <>(SELECT e1.salary FROM employees e1 ORDER BY e1.salary DESC LIMIT 1 
) ORDER BY e2.salary DESC LIMIT 1; 


SELECT e.first_name, e.last_name FROM projects p
JOIN employees_projects ep ON ep.project_id = p.id
JOIN employees e on e.id = employee_id
WHERE  p.title = 'Build a cool site';


SELECT e.first_name, e.last_name, 
((datediff(p.end_date,p.start_date)/15)* (e.salary/(365))*15) as project_total_payment
FROM projects p
JOIN employees_projects ep ON ep.project_id = p.id
JOIN employees e on e.id = employee_id
WHERE  p.title = 'Build a cool site';




