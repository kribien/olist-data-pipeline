SELECT
    products.product_id,
    products.product_category_name,
    CASE
        WHEN translations.product_category_name_english IS NOT NULL
            THEN translations.product_category_name_english
        ELSE products.product_category_name
    END AS product_category
FROM {{ ref('stg_products') }} AS products
LEFT JOIN {{ ref('stg_category_translation') }} AS translations
    ON products.product_category_name = translations.product_category_name