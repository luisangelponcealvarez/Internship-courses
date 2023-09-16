SELECT *
FROM Customers
WHERE CustomerID >= 50
  AND NOT Country = "Germany"
-- LIMIT 5;
SELECT *
FROM Products
WHERE NOT CategoryID = 6
  AND NOT SupplierID = 1
  AND Price <= 30
ORDER BY random()
-- LIMIT 3;