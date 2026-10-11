SELECT

    
CAST(order_items.order_id AS VARCHAR)
        || '-'
        || CAST(order_items.order_item_id AS VARCHAR) AS order_item_key,
    order_items.order_id,
    order_items.order_item_id,
    orders.customer_id,
    order_items.product_id,
    order_items.seller_id,
    orders.order_status,
    orders.order_purchase_timestamp,
    orders.order_approved_at,
    order_items.shipping_limit_date,
    order_items.item_price,
    order_items.freight_value,
    order_items.item_price + order_items.freight_value AS gross_item_value
FROM {{ ref('stg_order_items') }} AS order_items
INNER JOIN {{ ref('stg_orders') }} AS orders
    ON order_items.order_id = orders.order_id