with customer_last_90_day_purchases as (
    select
    o.customer_id as customer_id
    , max(o.delivered_date) as last_delivery_date
    , min(o.delivered_date) as first_delivery_date
    , sum(o.order_subtotal) as total_order_revenue
    , count(distinct o.id) as count_of_unique_order_ids
    FROM ANALYTICS.PRODUCTION.ORDERS o
    group by 1
)

select
c.id as customer_id
, case when count_of_unique_order_ids > 0 then 'active' else 'inactive' end as customer_status
, p.last_delivery_date as last_delivery_date
, p.total_order_revenue as total_order_revenue
, TIMESTAMPDIFF(day, p.first_delivery_date, p.last_delivery_date) as days_between_first_and_last_order
, RANK() over (partition by c.id order by total_order_revenue desc) as customer_revenue_rank
, c.*
FROM ANALYTICS.PRODUCTION.CUSTOMERS c
LEFT JOIN customer_last_90_day_purchases p on c.id = p.customer_id
WHERE c.billing_details_status = 'authenticated'
AND c.customer_created_timestamp > date('2020-01-01')
ORDER BY c.customer_created_timestamp desc