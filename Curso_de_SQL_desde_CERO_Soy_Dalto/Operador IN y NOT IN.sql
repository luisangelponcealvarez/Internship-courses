/*Esta es una manera de selecciónar*/
SELECT * FROM Products
WHERE SupplierID = 3
OR SupplierID = 4
OR SupplierID = 5
OR SupplierID = 6;
/*Esta es otra manera de selecciónar mas corta*/
SELECT * FROM Products
WHERE SupplierID IN (3,4,5,6)