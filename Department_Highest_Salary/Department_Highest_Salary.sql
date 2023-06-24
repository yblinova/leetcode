with table1 as (
select  id , name  ,  max(salary) over (partition by departmentId) salary_max , salary , departmentId
from employee
)

select d.name as Department , t.name as  Employee , t.salary as Salary
from table1 t left join department d on t.departmentId = d.id
where t.salary = t.salary_max