with t1 as (
  select id, num , lead(num) over (order by id) ld1, lead(num, 2)  over (order by id) ld2
  from logs
)

select distinct num as ConsecutiveNums
from t1 
where num = ld1 and num = ld2