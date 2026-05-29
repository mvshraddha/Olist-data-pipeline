{{ config(materialized='table') }}

SELECT
    o.order_id,
    
    o.customer_id,

    c.customer_city,

    c.customer_state,

    o.order_purchase_timestamp,

    o.order_status

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('stg_customers') }} c
ON o.customer_id = c.customer_id

WHERE o.order_status = 'delivered'