SELECT
    order_id,
    TRY_CAST(order_item_id AS INTEGER) AS order_item_id,
    product_id,
    seller_id,
    TRY_CAST(shipping_limit_date AS TIMESTAMP) AS shipping_limit_date,
    TRY_CAST(price AS DECIMAL(18, 2)) AS item_price,
    TRY_CAST(freight_value AS DECIMAL(18, 2)) AS freight_value
FROM {{ source('olist_raw', 'order_items') }}