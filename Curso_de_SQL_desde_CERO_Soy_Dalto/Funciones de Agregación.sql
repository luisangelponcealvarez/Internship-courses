/*la cantidad de nombres que hay*/
SELECT count(FirstName) as Cantidad_de_nombres FROM Employees;
/*la suma de los price*/
SELECT sum(Price) as Total FROM Products;
/*redondeando el promedio*/
SELECT round(avg(Price)) as Promedio FROM Products;
/*promedio con los desimales que quieras*/
SELECT round(avg(price),1)as promedio FROM Products
