-- -- Table: items
-- CREATE TABLE items(
-- user_id SERIAL PRIMARY KEY,
-- items VARCHAR(100) NOT NULL,
-- price NUMERIC(10,2) NOT NULL)

-- -- Table: customers
-- CREATE TABLE customers(
-- user_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(100) NOT NULL,
-- last_name VARCHAR(100) NOT NULL)

-- -- Insert sample data into items table
-- INSERT INTO items
-- (user_id, items, price)
-- VALUES 
-- (1, 'Small Desk', 100),
-- (2, 'Large desk', 300),
-- (3, 'Fan', 80);

-- -- Insert sample data into customers table
-- INSERT INTO customers
-- (user_id, first_name, last_name)
-- VALUES 
-- (1 ,'Greg' ,'Jones'),
-- (2 ,'Sandra' ,'Jones'),
-- (3 ,'Scott' ,'Scott'),
-- (4 ,'Trevor' ,'Green'),
-- (5 ,'Melanie' ,'Johnson')

-- Use SQL to fetch the following data from the database:

-- All the items.
-- select * from customers;
-- select * from items;

-- All the items with a price above 80 (80 not included).
-- SELECT * FROM items
-- WHERE price >= 80

-- All the items with a price below 300. (300 included)
-- SELECT * FROM items
-- WHERE price >= 300

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- SELECT * FROM customers 
-- WHERE last_name LIKE ('Smith')
-- output is null table

-- All customers whose last name is ‘Jones’.
-- SELECT * FROM customers 
-- WHERE last_name LIKE ('Jones')

-- All customers whose firstname is not ‘Scott’.
-- SELECT * FROM customers 
-- WHERE last_name NOT IN ('Scott')



