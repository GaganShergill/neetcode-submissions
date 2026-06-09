-- Write your query below
select 
    first_name,
    last_name,
    city,
    state
from person
left join address on address.person_id = person.person_id