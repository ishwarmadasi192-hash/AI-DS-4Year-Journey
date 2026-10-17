create database practice_questions;
use practice_questions;

create schema customer_table;
create table customer_table.isolate(firstname varchar(10), last_name varchar(20),email varchar(50),address varchar(50),city varchar(10),state varchar(20),zip int);
-- by sir is down
create table customer(
customer_id int primary key,
first_name varchar(10),
last_name varchar(10),
email varchar(20),
adredd varchar(50),
city varchar(10),
state varchar(10),
zip char(6)
)
drop table customer;
create table customer(

customer_id int primary key,
first_name varchar(50),
last_name varchar(50),
email varchar(100),
address varchar(100),
city varchar(50),
state varchar(100),
zip char(6)
)

INSERT INTO customer (customer_id, first_name, last_name, email, address, city, state, zip)
VALUES
(1, 'Ravi', 'Miller', 'george.miller@gmail.com', '123 Elm St', 'SanJose', 'CA', '951126'),
(2, 'Grace', 'Anderson', 'grace.anderson@yahoo.com', '45 Oak Ave', 'SanJose', 'CA', '951236'),
(3, 'Gary', 'Holt', 'gary.holt@gmail.com', '78 Pine Rd', 'LosAngeles', 'CA', '900019'),
(4, 'Rosy', 'Garcia', 'linda.garcia@gmail.com', '56 Maple St', 'SanJose', 'CA', '951100'),
(5, 'David', 'Brown', 'david.brown@hotmail.com', '90 Birch Blvd', 'Sacramento', 'CA', '958142');

select * from customer;

-- select only first name and last name column from customer
select first_name,last_name from customer;

--Select those records where ‘first_name’ starts with “G” and city is ‘SanJose’
select * from customer where first_name like 'G%'
and city='SanJose';

--Select those records where Email contains ‘gmail’.
select * from customer
where email like '%gmail%';
--Select those records where the ‘last_name’ doesn't end with “A”
select * from customer
where last_name not like '%a';

--Create an ‘Orders’ table which comprises of these columns: ‘order_id’, ‘order_date’, ‘amount’, ‘customer_id’.Make amount as decimal.
create table orders(
order_id int,
order_Date date,
amount decimal(10,2),
customer_id int primary key
);
select * from customer;