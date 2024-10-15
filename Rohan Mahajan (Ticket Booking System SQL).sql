create database shoppie;

use shoppie;

create table customers(
customer_id int not null primary key,
firstname varchar(10) not null,
lastname varchar(10),
email varchar(20) not null,
phone varchar(12),
address varchar(30));

create table products(
product_id int primary key,
name varchar(20) not null,
description varchar(30),
price float not null);

create table orders(
order_id int primary key,
customer_id int,
order_date date not null,
constraint fk_orders_customers foreign key (customer_id)
references customers(customer_id)
);

create table orderDetails(  
orderDetails_id int primary key,
order_id int,  
product_id int,
quantity int not null,
constraint fk_orderDetails_orders foreign key (order_id)
references orders(order_id),
constraint fk_orderDetails_products foreign key (product_id)
references products(product_id));

create table inventory(
inventory_id int primary key,
product_id int,
quantityInStock int, 
lastStockUpdate date,
constraint fk_inventory_products foreign key(product_id)
references products(product_id)
);
 

 insert into customers (customer_id, firstname, lastname, email, phone, address) values
(1, 'Ravi', 'Sharma', 'ravi@examp.com', '9876543210', '123 MG Road, Bangalore'),
(2, 'Pooja', 'Verma', 'pooja@examp.com', '8765432109', '456 Park Street, Kolkata'),
(3, 'Vikas', 'Patel', 'vikas@examp.com', '7654321098', '789 Marine Drive, Mumbai'),
(4, 'Anjali', 'Mehta', 'anjali@examp.com', '6543210987', '321 Connaught Place, New Delhi'),
(5, 'Amit', 'Sinha', 'amit@examp.com', '5432109876', '654 Brigade Road, Bangalore'),
(6, 'Priya', 'Singh', 'priya@examp.com', '4321098765', '987 Juhu Beach Road, Mumbai'),
(7, 'Rahul', 'Kapoor', 'rahul@examp.com', '3210987654', '456 Banjara Hills, Hyderabad'),
(8, 'Nidhi', 'Chopra', 'nidhi@examp.com', '2109876543', '789 MG Road, Pune'),
(9, 'Deepak', 'Sharma', 'deepak@examp.com', '1098765432', '321 Sector 17, Chandigarh'),
(10, 'Neha', 'Malhotra', 'neha@examp.com', '0987654321', '654 Vasant Kunj, New Delhi');

 insert into products (product_id, name, description, price) values
(1, 'Smartphone', 'High-end smartphone', 59999.99),
(2, 'Laptop', '15-inch gaming laptop', 79999.99),
(3, 'Tablet', '10-inch tablet', 24999.99),
(4, 'Smartwatch', 'Waterproof smartwatch', 19999.99),
(5, 'Headphones', 'Noise-canceling headphones', 7999.99),
(6, 'Gaming Console', 'Next-gen gaming console', 49999.99),
(7, 'Digital Camera', 'DSLR camera with 24MP', 59999.99),
(8, 'Wireless Speaker', 'Bluetooth speaker', 4999.99),
(9, 'External Hard Drive', '1TB hard drive', 3999.99),
(10, 'VR Headset', 'Virtual reality headset', 29999.99);

 insert into orders (order_id, customer_id, order_date) values
(1, 1, '2023-08-01'),
(2, 2, '2023-08-02'),
(3, 3, '2023-08-03'),
(4, 4, '2023-08-04'),
(5, 5, '2023-08-05'),
(6, 6, '2023-08-06'),
(7, 7, '2023-08-07'),
(8, 8, '2023-08-08'),
(9, 9, '2023-08-09'),
(10, 10, '2023-08-10');

 insert into orderDetails (orderDetails_id, order_id, product_id, quantity) values
(1, 1, 1, 1),
(2, 2, 2, 1), 
(3, 3, 3, 2), 
(4, 4, 4, 1), 
(5, 5, 5, 2), 
(6, 6, 6, 1), 
(7, 7, 7, 1), 
(8, 8, 8, 1), 
(9, 9, 9, 3),
(10, 10, 10, 1);

 insert into inventory (inventory_id, product_id, quantityInStock, lastStockUpdate) values
(1, 1, 100, '2023-07-31'),
(2, 2, 50, '2023-07-31'),
(3, 3, 75, '2023-07-31'),
(4, 4, 30, '2023-07-31'),
(5, 5, 60, '2023-07-31'),
(6, 6, 40, '2023-07-31'),
(7, 7, 25, '2023-07-31'),
(8, 8, 80, '2023-07-31'),
(9, 9, 100, '2023-07-31'),
(10, 10, 20, '2023-07-31');

select firstName+' '+lastName as name
,email from customers;  

select orders.order_id, orders.order_date, customers.firstname+' '+customers.lastname as customer_name
from orders, customers
where orders.customer_id = customers.customer_id

insert into customers(customer_id, firstname, lastname, email, phone, address) values
(11, 'Prince', 'Patel', 'prince@example.com', '912346780', '123, Sector 2, Jhansi'); 

update products 
set price = price+price*0.1
where product_id>=1;

select * from products;

declare @orderId int = 8
delete from orderDetails where order_id = @orderId 
--as here order_id is foreign key, we need to delete it from child first
delete from orders where order_id = @orderId; 
--then only we can delete it from parent.

select * from orders;

insert into orders (order_id, customer_id, order_date) values
(8, 2, '2023-8-11');

select * from orders;

update customers 
set email = 'patelji@example.com', phone = '9874563210', address = '53, Hinjewadi, Pune'
where customer_id = 3;

select * from customers
where customer_id<=5;

alter table orders add totalAmount float;

update orders
set totalAmount = (select sum(orderDetails.quantity*(select price from products where products.product_id=orderDetails.product_id ))
from orderDetails where orderDetails.order_id = orders.order_id);

select * from orders;

declare @custId int = 6
declare @oId int = (select order_id from orders where customer_id = @custId)
delete from orderDetails where order_id = @oId
delete from orders where customer_id = @custId

select * from orderDetails


insert into products(product_id, name, description, price) values
(11, 'Smart Watch', 'Bluetooth calling, camera', 9999.999);

select * from products

alter table orders 
add status varchar(20);

update orders
set status = ('Pending')
where order_id >=1;

update orders 
set status = 'Shipped'
where order_id <= 3;

select * from orders

