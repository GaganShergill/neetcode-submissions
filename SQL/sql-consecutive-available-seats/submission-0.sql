-- Write your query below
with consecutive_check as (
    select
        seat_id,
        lag(seat_id) over (order by seat_id) as prev_seat_id,
        lead(seat_id) over (order by seat_id) as next_seat_id
    from cinema
    where free = 1
)
select seat_id from consecutive_check
where prev_seat_id = seat_id - 1
    or next_seat_id = seat_id + 1