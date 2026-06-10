-- Write your query below
-- let's take immediate as 1 and scheduled as Null
select round(
    100.0 * sum(
            case
                when customer_pref_delivery_date = order_date then 1
                else 0
            end
        ) / count(*), 2
    ) as immediate_percentage
from delivery
