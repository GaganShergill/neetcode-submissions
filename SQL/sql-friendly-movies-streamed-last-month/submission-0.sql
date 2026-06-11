-- Write your query below
select distinct title
from content c
where kids_content = 'Y'
    and content_type = 'Movies'
    and exists (
        select 1
        from tv_program t
        where t.content_id = c.content_id
            and program_date >= '2020-06-01' and program_date < '2020-07-01'
    )