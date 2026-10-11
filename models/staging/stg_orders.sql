SELECT
    order_id,
    customer_id,
    order_status,
    TRY_CAST(order_purchase_timestamp AS TIMESTAMP) AS order_purchase_timestamp,
    TRY_CAST(order_approved_at AS TIMESTAMP) AS order_approved_at
FROM {{ source('olist_raw', 'orders') }}