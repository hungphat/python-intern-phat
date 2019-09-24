-- Create Table
CREATE TABLE CUSTOMERS(
	id int PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	birth DATE NOT NULL ,
	address VARCHAR(50),
	phone VARCHAR(20),
	update timestamp
);


