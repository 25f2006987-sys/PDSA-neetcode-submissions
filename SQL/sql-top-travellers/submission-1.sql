-- Write your query below
select u.name, coalesce (sum(r.distance),0) as travelled_distance from rides r right outer join users u on u.id=r.user_id
group by u.id, u.name order by travelled_distance desc, u.name asc
