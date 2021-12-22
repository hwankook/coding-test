select a.request_at                                                                    as 'Day'
     , round(sum(case when status = 'completed' then 0 else 1 end) / count(status), 2) as 'Cancellation Rate'
from (
       select a.request_at
            , a.status
         from Trips a
        where client_id = (select users_id from Users where users_id = client_id and banned = 'No')
          and driver_id = (select users_id from Users where users_id = driver_id and banned = 'No')
     ) a
 where a.request_at between '2013-10-01' and '2013-10-03'
 group by a.request_at
;