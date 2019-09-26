--03. Show Lowest Customer Age

SELECT * FROM customers
WHERE birth = (SELECT max(birth) as yongest_customer FROM customers);