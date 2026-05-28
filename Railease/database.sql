CREATE DATABASE railway_system;
USE railway_system;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE trains(
    train_no INT PRIMARY KEY,
    train_name VARCHAR(100),
    source VARCHAR(50),
    destination VARCHAR(50),
    departure TIME,
    arrival TIME,
    total_seats INT,
    available_seats INT,
    fare DECIMAL(10,2)
);


CREATE TABLE bookings(
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    train_no INT,
    passenger_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    seat_no VARCHAR(20),
    journey_date DATE,
    pnr VARCHAR(20)
);
INSERT INTO trains(
train_no,
train_name,
source,
destination,
departure,
arrival,
total_seats,
available_seats,
fare
)
VALUES
(12951,'Mumbai Rajdhani','New Delhi','Mumbai','16:35:00','08:35:00',72,45,2720.00),
(12627,'Karnataka Express','New Delhi','Bangalore','21:15:00','13:10:00',72,31,2410.00),
(16382,'Kerala Express','New Delhi','Thiruvananthapuram','11:25:00','15:45:00',72,22,1760.00),
(12237,'Duronto Express','New Delhi','Mumbai','23:00:00','14:30:00',72,18,3070.00),
(12138,'Punjab Mail','New Delhi','Mumbai','05:10:00','04:20:00',72,14,1360.00),
(22436,'Vande Bharat Express','Delhi','Varanasi','06:00:00','14:00:00',72,40,2200.00),
(12002,'Shatabdi Express','Delhi','Bhopal','06:15:00','14:25:00',72,55,1650.00),
(12841,'Coromandel Express','Kolkata','Chennai','14:50:00','16:15:00',72,28,1950.00),
(12625,'Kerala SF Express','Thiruvananthapuram','Delhi','11:15:00','16:50:00',72,37,2100.00),
(16345,'Netravati Express','Mumbai','Mangalore','11:40:00','06:45:00',72,44,1450.00),
(12618,'Mangala Lakshadweep Express','Delhi','Ernakulam','13:15:00','10:30:00',72,35,2250.00),
(16525,'Island Express','Bangalore','Kanniyakumari','06:25:00','20:35:00',72,41,1300.00),
(12779,'Goa Express','Delhi','Goa','15:00:00','05:30:00',72,39,1980.00),
(12301,'Howrah Rajdhani','Delhi','Kolkata','16:55:00','10:05:00',72,26,2700.00),
(22691,'Rajdhani Express','Bangalore','Delhi','20:00:00','05:55:00',72,29,2850.00),
(12953,'August Kranti Rajdhani','Mumbai','Delhi','17:40:00','09:55:00',72,33,3100.00);

INSERT INTO users(name,email,password,phone)
VALUES(
'Anvitha',
'anvi@gmail.com',
'1234',
'9876543210'
);