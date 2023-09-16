SELECT FirstName, LastName,
  (
	SELECT sum(od.Quantity)
  from [Orders] o, [OrderDetails] od
  WHERE o.EmployeeID = e.EmployeeID AND od.OrderID = o.OrderID
  ) as unidades_totales

FROM [Employees] e

WHERE unidades_totales > (SELECT AVG (unidades_totales)
FROM ( 
  SELECT (
  (
	SELECT SUM(od.Quantity)
    FROM [Orders] o, [OrderDetails] od
    WHERE o.EmployeeID = e2.EmployeeID AND od.OrderID = o.OrderID
  ) 
  ) AS unidades_totales
  FROM [Employees] e2
  GROUP BY e2.EmployeeID
))