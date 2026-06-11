-- Write your query below
select 
    date_id,
    make_name,
    count(distinct lead_id) unique_leads,
    count(distinct partner_id) unique_partners
from daily_sales
group by date_id, make_name