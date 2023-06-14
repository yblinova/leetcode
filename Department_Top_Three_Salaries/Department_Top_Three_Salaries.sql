select d.name as Department , Employee , salary as Salary
from (
  select departmentId as Department , name as Employee , salary, 
  dense_rank() over (partition by departmentId order by salary desc) as rn
  from Employee ) e left join Department d on e.Department = d.id
where rn <= 3