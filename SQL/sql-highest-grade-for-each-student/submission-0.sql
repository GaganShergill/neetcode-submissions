-- Write your query below
with ranked_exams as (
    select student_id, exam_id, score,
        row_number() over (
            partition by student_id
            order by score desc, exam_id asc
    ) as score_rank from exam_results
)
select student_id, exam_id, score from ranked_exams
where score_rank = 1
order by student_id