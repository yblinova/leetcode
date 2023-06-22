with t1 as (
    select * , 
        lead(id) over (order by id) ld , 
        lead(id , 2) over (order by id) ld2 , 
        lag(id) over (order by id) lg, 
        lag(id , 2) over (order by id) lg2
    from Stadium
    where people >= 100
    order by visit_date asc
)

select id , visit_date , people
from t1
where (ld = (id +1) and ld2 = (id +2)) or (lg = (id - 1 )and lg2 = (id - 2)) or (ld = (id +1) and lg = (id  -1))