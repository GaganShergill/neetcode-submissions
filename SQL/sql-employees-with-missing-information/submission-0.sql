-- Write your query below
select
    case
        when e.employee_id is null then s.employee_id
        else e.employee_id
    end as employee_id
from employees e
full join salaries s on e.employee_id = s.employee_id
where e.name is null or s.salary is null;