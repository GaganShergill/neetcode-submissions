-- Write your query below
with merge_tbl as (
    select 
        host_team as team_id,
        case
            when host_goals > guest_goals then 3
            when host_goals = guest_goals then 1
            else 0
        end as num_points
    from matches
    union all
    select
        guest_team as team_id, 
        case
            when guest_goals > host_goals then 3
            when guest_goals = host_goals then 1
            else 0
        end as num_points
    from matches
)
select
    t.team_id, t.team_name, coalesce(sum(m.num_points), 0) as num_points
from merge_tbl m
right join teams t on m.team_id = t.team_id
group by t.team_id, t.team_name
order by num_points desc, t.team_id
