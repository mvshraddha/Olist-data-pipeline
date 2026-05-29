{{ config(materialized='view') }}

SELECT
    customer_id,
    
    customer_unique_id,

    customer_zip_code_prefix
        AS zip_code,

    LOWER(customer_city)
        AS customer_city,

    UPPER(customer_state)
        AS customer_state

FROM customers_raw

WHERE customer_id IS NOT NULL