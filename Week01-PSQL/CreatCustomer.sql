--00. Create Database
Create database Sqlpostgres;

-- Create Table
Create table Customer(
	CustomerName varchar(100) primary key,
	Address varchar(max),
	Age int not null
);

--02. Insert Customer info

insert into Customer (CustomerName,Address,Age) values('A','Sai Gon','20');
insert into Customer (CustomerName,Address,Age) values('B','Ha Noi','30');
insert into Customer (CustomerName,Address,Age) values('C','Sai Gon','10');
insert into Customer (CustomerName,Address,Age) values('D','Sai Gon','50');

--03. Show Lowest Customer Age

SELECT MIN(age) AS YoungestCustomer 
WHERE age = (SELECT MIN(Age) as LowestAge FROM Customer)







