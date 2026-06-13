-- Write your query below
select
    COALESCE(e.employee_id, s.employee_id) AS employee_id
from employees e
full join salaries s on e.employee_id = s.employee_id
where e.name is null or s.salary is null
order by employee_id;