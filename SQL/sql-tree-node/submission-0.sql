-- Write your query below
-- root if p_id is null
-- inner if p_id is not null and id exists as p_id in any other row
-- leaf if p_id is not null and id not exists as p_id in any other row
with parent_nodes as (
    select p.id from tree p
    where exists (
        select 1 from tree t
        where t.p_id = p.id
    )
)
select
    t.id,
    case
        when t.p_id is null then 'Root'
        when p.id is null then 'Leaf'
        else 'Inner'
    end as type
from tree t
left join parent_nodes p on t.id = p.id

