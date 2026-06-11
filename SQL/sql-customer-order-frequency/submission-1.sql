-- Write your query below
with base_tbl as (
    select 
        c.customer_id,
        c.name
    from customers c
    join orders o on c.customer_id = o.customer_id
    join product p on o.product_id = p.product_id
    where o.order_date >= '2020-06-01' and o.order_date < '2020-08-01'
    group by c.customer_id, c.name, date_trunc('month', o.order_date)
    having sum(o.quantity*p.price) >= 100
)
select
    customer_id, name
from base_tbl
group by customer_id, name
having count(*) = 2