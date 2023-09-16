SELECT SupplierID, round(avg(Price)) AS promedio FROM Products
WHERE ProductName IS NOT NULL
GROUP BY SupplierID
HAVING promedio > 40;

SELECT ProductID, sum(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
ORDER BY total DESC
LIMIT 1