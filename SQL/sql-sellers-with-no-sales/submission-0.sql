-- Write your query below
SELECT distinct s.seller_name from seller s WHERE
NOT EXISTS (
    select 1 from orders o WHERE s.seller_id=o.seller_id and o.sale_date between '2020-01-01' and '2020-12-31'
)
