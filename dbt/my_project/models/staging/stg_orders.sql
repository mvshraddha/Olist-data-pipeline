{{ config(materialized='view') }}

SELECT
    order_id,
    customer_id,
    order_status,

    TRY_TO_TIMESTAMP(order_purchase_timestamp)
        AS order_purchase_timestamp,

    TRY_TO_TIMESTAMP(order_approved_at)
        AS order_approved_at,

    TRY_TO_TIMESTAMP(order_delivered_carrier_date)
        AS order_delivered_carrier_date,

    TRY_TO_TIMESTAMP(order_delivered_customer_date)
        AS order_delivered_customer_date,

    TRY_TO_TIMESTAMP(order_estimated_delivery_date)
        AS order_estimated_delivery_date

FROM orders_raw

WHERE order_id IS NOT NULL