-- Este comando es para encontrar el price minimo
SELECT ProductName, min(Price) FROM Products
WHERE ProductName IS NOT NULL;
-- Este comando es para encontrar el price maximo
SELECT ProductName, max(Price) FROM Products