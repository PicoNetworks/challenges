CREATE TABLE IF NOT EXISTS customers(
   customer_id              VARCHAR(32) NOT NULL PRIMARY KEY 
  ,customer_unique_id       VARCHAR(32) NOT NULL
  ,customer_zip_code_prefix INTEGER  NOT NULL
  ,customer_city            VARCHAR(32) NOT NULL
  ,customer_state           VARCHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
   product_id                 VARCHAR(32) NOT NULL PRIMARY KEY
  ,product_category_name      VARCHAR(46)
  ,product_name_lenght        INTEGER 
  ,product_description_lenght INTEGER 
  ,product_photos_qty         INTEGER 
  ,product_weight_g           INTEGER 
  ,product_length_cm          INTEGER 
  ,product_height_cm          INTEGER 
  ,product_width_cm           INTEGER 
);


CREATE TABLE IF NOT EXISTS orders(
   order_id                      VARCHAR(32) NOT NULL PRIMARY KEY
  ,customer_id                   VARCHAR(32) references customers(customer_id)
  ,order_status                  VARCHAR(11) NOT NULL
  ,order_purchase_timestamp      VARCHAR(19) NOT NULL
  ,order_approved_at             VARCHAR(19)
  ,order_delivered_carrier_date  VARCHAR(19)
  ,order_delivered_customer_date VARCHAR(19)
  ,order_estimated_delivery_date VARCHAR(19) NOT NULL
);


CREATE TABLE IF NOT EXISTS sellers(
   seller_id              VARCHAR(32) NOT NULL PRIMARY KEY
  ,seller_zip_code_prefix INTEGER  NOT NULL
  ,seller_city            VARCHAR(40) NOT NULL
  ,seller_state           VARCHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS order_items(
   order_id            VARCHAR(32) references orders(order_id)
  ,order_item_id       INTEGER  NOT NULL 
  ,product_id          VARCHAR(32) references products(product_id)
  ,seller_id           VARCHAR(32) NOT NULL
  ,shipping_limit_date TIMESTAMP NOT NULL
  ,price               NUMERIC(7,2) NOT NULL
  ,freight_value       NUMERIC(6,2) NOT NULL
);


CREATE TABLE IF NOT EXISTS order_reviews(
   review_id               VARCHAR(32) NOT NULL PRIMARY KEY
  ,order_id                VARCHAR(32) references orders(order_id)
  ,review_score            INTEGER  NOT NULL
  ,review_comment_title    VARCHAR(26)
  ,review_comment_message  VARCHAR(208)
  ,review_creation_date    TIMESTAMP NOT NULL
  ,review_answer_timestamp TIMESTAMP NOT NULL
);
