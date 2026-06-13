-- Write your query below
select
    p.product_id,
    u.store,
    u.price
from products p
cross join lateral (
    values
        ('store1', p.store1),
        ('store2', p.store2),
        ('store3', p.store3)
) as u(store, price)
where u.price is not null;