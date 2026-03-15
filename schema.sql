CREATE DATABASE sales_pipeline;
USE sales_pipeline;


CREATE TABLE sales_data (

row_id INT,
order_id VARCHAR(50),
order_date DATE,
ship_date DATE,
ship_mode VARCHAR(50),

customer_id VARCHAR(50),
customer_name VARCHAR(100),
segment VARCHAR(50),

country_region VARCHAR(100),
city VARCHAR(100),
state VARCHAR(100),
postal_code VARCHAR(20),
region VARCHAR(50),

product_id VARCHAR(50),
category VARCHAR(50),
sub_category VARCHAR(50),
product_name VARCHAR(200),

sales FLOAT,
quantity INT,
discount FLOAT,
profit FLOAT

);