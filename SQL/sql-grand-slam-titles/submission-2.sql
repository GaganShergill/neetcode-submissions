-- Write your query below
with up_championships as (
    select
        c.year,
        u.player_id
    from championships c
    cross join lateral (
        values
            (c.wimbledon),
            (c.fr_open),
            (c.us_open),
            (c.au_open)
    ) u(player_id)
)
select
    c.player_id,
    p.player_name,
    count(*) as grand_slams_count
from up_championships c
join players p on c.player_id = p.player_id 
group by c.player_id, p.player_name

