import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("usuarios.sql")
query = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) AS Total
    FROM Orders o
    JOIN Employee e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
''' 


top_employees = pd.read_sql(query,conn)
top_employees.plot(x='Employee',y='Total',kind='bar',figsize=(10,10),legend=False)

plt.show()