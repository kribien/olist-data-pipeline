SELECT
    product_category_name,
    product_category_name_english
FROM {{ source('olist_raw', 'product_category_translation') }}