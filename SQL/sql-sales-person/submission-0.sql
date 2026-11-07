-- Write your query below
select p.name from sales_person p where p.sales_id not in
(select o.sales_id from orders o, company c where c.name='CRIMSON' and o.com_id=c.com_id)