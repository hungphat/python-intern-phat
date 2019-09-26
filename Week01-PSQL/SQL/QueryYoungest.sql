--03. Show Lowest Customer Age
--TODO lower and upper case is inconsistent for name of table
SELECT * FROM CUSTOMERS
WHERE birth = (SELECT max(birth) as EarliestDate FROM customers);