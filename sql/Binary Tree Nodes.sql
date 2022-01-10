-- Language: Oracle
select  a.n,
        decode(a.p, null, 'Root', decode(b.p, null, 'Leaf', 'Inner'))
from    BST a,
        (
        select  p
        from    BST
        group by p
        ) b
where   a.n = b.p(+)
order by a.n
;
