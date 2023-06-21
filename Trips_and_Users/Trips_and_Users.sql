with t1 as (
  select request_at, count(*) cnt_total
  from trips 
  where client_id in (select users_id from users where banned = "No" ) and
  driver_id in (select users_id from users where banned = "No" ) and
  request_at between "2013-10-01" and "2013-10-03"
  group by request_at
),
t2 as (
  select request_at, count(*) cnt_canc
  from trips 
  where client_id in (select users_id from users where banned = "No" ) and
  driver_id in (select users_id from users where banned = "No" ) and 
  status like '%cancelled%' and
  request_at between "2013-10-01" and "2013-10-03"  
  group by request_at

)

select t1.request_at as Day, round ((coalesce (t2.cnt_canc , 0)/t1.cnt_total) , 2) as 'Cancellation Rate'
from t1 left join t2 on t1.request_at = t2.request_at