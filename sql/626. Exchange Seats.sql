select b.id,
       ifnull((select student from Seat where id = a.id + a.row_id), b.student) as student
  from (
       select id,
              case
                  when mod(id, 2) = 1 then  1
                  when mod(id, 2) = 0 then -1
              end as row_id
         from Seat
       ) a,
       Seat b
 where b.id = a.id
 order by b.id
;

select row_number() over w as id,
       student
  from Seat
window w as (order by if(mod(id, 2) = 1, id + 1, id - 1))
;