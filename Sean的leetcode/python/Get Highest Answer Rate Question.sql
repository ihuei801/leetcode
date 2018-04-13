# Write your MySQL query statement below
select question_id as survey_log 
from
(
    select question_id, sum(case when action='show' then 1 else 0 end) as s_ct, sum(case when action='answer' then 1 else 0 end) as a_ct from survey_log group by question_id 
) as tb1
order by (a_ct/s_ct) desc limit 1

  