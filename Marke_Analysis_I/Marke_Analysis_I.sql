select u.user_id as buyer_id  , u.join_date , 
  sum(case 
  when o.order_date like '2019%' then 1 
  else 0
  end) orders_in_2019
from orders o right join users u on u.user_id = o.buyer_id
group by u.user_id , u.join_date