--03. Show Lowest Customer Age

SELECT * FROM CUSTOMERS
WHERE birth = (SELECT max(birth) as EarliestDate FROM customers);