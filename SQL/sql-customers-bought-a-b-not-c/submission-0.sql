-- Write your query below
select distinct c.customer_id, c.customer_name from customers c
where 
EXISTS
(select o.order_id from  orders o where c.customer_id = o.customer_id and o.product_name in('B'))

AND
EXISTS
(select o.order_id from  orders o where c.customer_id = o.customer_id and o.product_name in('A'))


AND  
NOT EXISTS
(select o.order_id from orders o where c.customer_id = o.customer_id and o.product_name in('C'))

order by c.customer_name