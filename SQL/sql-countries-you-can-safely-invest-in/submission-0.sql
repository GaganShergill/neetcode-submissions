-- Write your query below
-- average call duration - globally
-- average call duration - per country - same country caller and callee
-- output country which has local avg duration > global avg duration

with base_tbl as (
    select
        cn1.name, c.duration
    from calls c
    join person p1 on c.caller_id = p1.id
    join country cn1 on left(p1.phone_number, 3) = cn1.country_code

    union all

    select
        cn2.name, c.duration
    from calls c
    join person p2 on c.callee_id = p2.id
    join country cn2 on left(p2.phone_number, 3) = cn2.country_code 
)
select
    name as country
from base_tbl
group by name
having avg(duration) > (
    select avg(duration)
    from calls
)
