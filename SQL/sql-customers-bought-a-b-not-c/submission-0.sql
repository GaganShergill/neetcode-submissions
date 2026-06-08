-- Write your query below
select c.customer_id, c.customer_name
from customers c
where exists (
    select 1 from orders o
    where o.customer_id = c.customer_id
    and o.product_name in ('A', 'B', 'C')
    group by customer_id
    having max(case when product_name = 'A' then 1 else 0 end) = 1
    and max(case when product_name = 'B' then 1 else 0 end) = 1
    and max(case when product_name = 'C' then 1 else 0 end) = 0
)
order by customer_name