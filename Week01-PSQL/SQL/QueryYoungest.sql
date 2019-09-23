--03. Show Lowest Customer Age

SELECT MIN(age) AS YoungestCustomer
WHERE age = (SELECT MIN(Age) as LowestAge FROM Customer)


