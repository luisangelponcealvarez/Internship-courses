SELECT ProductID, Quantity,
 (SELECT ProductName FROM Products WHERE OrderDetails.ProductID = ProductID) as Nombre, 
 (SELECT Price FROM Products WHERE OrderDetails.ProductID = ProductID) as Precio
FROM OrderDetails;

SELECT ProductID, sum(Quantity) as total_vendido,
 (SELECT Price FROM Products WHERE ProductID = OD.ProductID) as Precio,
 (sum(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID)) as Total_Recaudado,
FROM [OrderDetails] OD
GROUP BY ProductID