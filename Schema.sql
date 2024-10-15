create database ticketbookingsystem;

use ticketbookingsystem;

-- venue table
create table venue (
    venue_id int primary key identity,
    venue_name nvarchar(100),
    address nvarchar(255)
);

-- event table
create table event (
    event_id int primary key identity,
    event_name nvarchar(100),
    event_date date,
    event_time time,
    venue_id int foreign key references venue(venue_id),
    total_seats int,
    available_seats int,
    ticket_price decimal(10, 2),
    event_type nvarchar(50) check (event_type in ('movie', 'concert', 'sports'))
);

-- customer table
create table customer (
    customer_id int primary key identity,
    customer_name nvarchar(100),
    email nvarchar(255),
    phone_number nvarchar(20)
);

-- booking table
create table booking (
    booking_id int primary key identity,
    customer_id int foreign key references customer(customer_id),
    event_id int foreign key references event(event_id),
    num_tickets int,
    total_cost decimal(10, 2),
    booking_date date
);

insert into venue (venue_name, address) values
('grand theater', '123 main st'),
('city auditorium', '456 market road'),
('open arena', '789 highland park'),
('rock stadium', '101 sports street'),
('classic hall', '333 king boulevard'),
('urban dome', '567 sunset boulevard'),
('national plaza', '245 liberty square'),
('blue horizon', '777 ocean view ave'),
('silver star hall', '987 elm street'),
('golden crown arena', '303 kings way');

select * from venue

insert into event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) values
('rock concert', '2024-11-01', '19:00:00', 4, 20000, 15000, 50.00, 'concert'),
('classical music night', '2024-12-05', '18:30:00', 2, 500, 200, 25.00, 'concert'),
('movie premiere', '2024-11-10', '20:00:00', 1, 300, 150, 15.00, 'movie'),
('basketball game', '2024-11-20', '18:00:00', 4, 15000, 12000, 75.00, 'sports'),
('opera night', '2024-12-01', '18:00:00', 5, 800, 600, 40.00, 'concert'),
('soccer final', '2024-11-28', '16:00:00', 4, 25000, 22000, 80.00, 'sports'),
('indie film festival', '2024-10-25', '18:30:00', 6, 400, 350, 20.00, 'movie'),
('stand-up comedy show', '2024-11-15', '20:00:00', 3, 1000, 850, 30.00, 'concert'),
('boxing championship', '2024-12-12', '21:00:00', 4, 15000, 10000, 90.00, 'sports'),
('ballet performance', '2024-12-20', '19:00:00', 5, 700, 500, 60.00, 'concert');

select * from event

insert into customer (customer_name, email, phone_number) values
('john doe', 'johndoe@example.com', '1234567890'),
('jane smith', 'janesmith@example.com', '0987654321'),
('robert brown', 'robertb@example.com', '1122334455'),
('linda white', 'lindaw@example.com', '6677889900'),
('michael scott', 'michaels@example.com', '9988776655'),
('pam beesly', 'pambeesly@example.com', '8877665544'),
('jim halpert', 'jimhalpert@example.com', '7766554433'),
('dwight schrute', 'dwightschrute@example.com', '6655443322'),
('stanley hudson', 'stanleyh@example.com', '5544332211'),
('phyllis vance', 'phyllisv@example.com', '4433221100');

select * from customer

insert into booking (customer_id, event_id, num_tickets, total_cost, booking_date) values
(1, 1, 2, 100.00, '2024-10-01'),
(2, 2, 3, 75.00, '2024-10-02'),
(3, 3, 4, 60.00, '2024-10-03'),
(4, 4, 5, 375.00, '2024-10-05'),
(5, 5, 1, 40.00, '2024-10-06'),
(6, 6, 3, 240.00, '2024-10-07'),
(7, 7, 2, 40.00, '2024-10-08'),
(8, 8, 6, 180.00, '2024-10-09'),
(9, 9, 4, 360.00, '2024-10-10'),
(10, 10, 2, 120.00, '2024-10-11');

select * from booking
