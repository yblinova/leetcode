with t as (
select requester_id as id, count(*) cnt
from RequestAccepted
group by requester_id
union all
select accepter_id as id, count(*) cnt
from RequestAccepted
group by accepter_id
)

select id , sum(cnt) as num
from t
group by id
order by num desc limit 1