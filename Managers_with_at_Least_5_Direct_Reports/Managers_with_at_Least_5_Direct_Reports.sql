with t1 as ( 
  select managerId as id
  from Employee 
  group by managerId having count(*) >= 5
)

select name
from employee
where id in (select id from t1)