with t1 as (
select pid 
from insurance 
where tiv_2015 in (
  select tiv_2015 
  from insurance 
  group by tiv_2015 having count(*) >1 )
) ,

t2 as (
select pid 
from insurance 
where (lat , lon) in (
  select lat , lon
  from insurance
  group by  lat , lon having count(*) >1)
 )

select round(sum(tiv_2016), 2) as tiv_2016
from insurance
where pid in (select pid from t1) and pid not in (select pid from t2)