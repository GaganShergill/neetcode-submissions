-- Write your query below
select min(distance) as shortest
from (
    select
        (lead(x) over(order by x) - x) as distance
    from point
);


