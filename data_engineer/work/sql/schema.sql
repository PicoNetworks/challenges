CREATE SCHEMA olist;
CREATE TABLE customers(
 customer_id VARCHAR(100),
 customer_unique_id VARCHAR(100),
 customer_zip_code_prefix INT NOT NULL,
 customer_city VARCHAR(100) NOT NULL,
 customer_state VARCHAR(100) NOT NULL
);
CREATE TABLE sellers(
 seller_id VARCHAR(100),
 seller_zip_code_prefix INT NOT NULL,
 seller_city VARCHAR(100) NOT NULL,
 seller_state VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE products(
 product_id VARCHAR(100),
 product_category_name VARCHAR(100) NOT NULL,
 product_name_lenght INTEGER,
 product_description_lenght INTEGER,
 product_photos_qty VARCHAR(100),
 product_weight_g NUMERIC,
 product_length_cm NUMERIC,
 product_height_cm NUMERIC,
 product_width_cm NUMERIC
);
CREATE TABLE orders(
 order_id VARCHAR(100),
 customer_id VARCHAR(100),
 order_status VARCHAR(100) NOT NULL,
 order_purchase_timestamp VARCHAR(100) NOT NULL,
 order_approved_at VARCHAR(100),
 order_delivered_carrier_date TIMESTAMP without TIME zone,
 order_delivered_customer_date TIMESTAMP without TIME zone,
 order_estimated_delivery_date TIMESTAMP without TIME zone
);
CREATE TABLE order_items(
 order_id VARCHAR(100),
 order_item_id NUMERIC ,
 product_id VARCHAR(100),
 seller_id VARCHAR(100),
 shipping_limit_date DATE,
 price NUMERIC,
 freight_value NUMERIC
);
CREATE TABLE order_reviews(
 review_id VARCHAR(100),
 order_id VARCHAR(100),
 review_score INT,
 review_comment_title VARCHAR(100),
 review_comment_message VARCHAR(100),
 review_creation_date DATE,
 review_answer_timestamp TIMESTAMP without TIME zone
)