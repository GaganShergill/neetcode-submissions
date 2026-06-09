-- Write your query below
select
    left_operand,
    operator,
    right_operand,
    case
        when operator = '<' then l.value < r.value
        when operator = '>' then l.value > r.value
        else l.value = r.value
    end as value
from expressions e
join variables l on e.left_operand = l.name
join variables r on e.right_operand = r.name
