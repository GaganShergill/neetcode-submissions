-- Write your query below
select name from customers c
where c.id not in (
    select o.customer_id
    from orders o
)