SELECT FirstName, Reward, Month
FROM Employees e
  INNER JOIN Rewards r ON e.EmployeeID = r.EmployeeID