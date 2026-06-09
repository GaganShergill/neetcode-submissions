-- Write your query below
select seller_name from seller s
where not exists (
    select 1
    from orders o
    where o.seller_id = s.seller_id
    and sale_date >= '2020-01-01' and sale_date < '2021-01-01'
)
order by seller_name