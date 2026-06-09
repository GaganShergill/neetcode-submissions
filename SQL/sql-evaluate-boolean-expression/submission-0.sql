-- Write your query below
with filled_left as (
    select
        left_operand,
        operator,
        right_operand,
        value as left_value
    from expressions e
    join variables v on e.left_operand = v.name
),
filled_right as (
    select
        left_operand,
        operator,
        right_operand,
        left_value,
        value as right_value
    from filled_left e
    join variables v on e.right_operand = v.name
)
select
    left_operand,
    operator,
    right_operand,
    case
        when operator = '<' then left_value < right_value
        when operator = '>' then left_value > right_value
        else left_value = right_value
    end as value
from filled_right
