import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Nordthwind.db")
query = '''
  SELECT ProductName, SUM(Price * Quantity) as Revenue
  FROM OrdersDetails od
  JOIN Products p ON p.ProductsID = od.ProductID
  Group BY od.ProductID
  ORDER BY Revenue DESC
  LIMIT 10
''' 


top_products = pd.read_sql_query(query,conn)

top_products.plot(x="productName", y="Revenue", kind="bar", figsize=(10, 5), length="False")


plt.title("10 Productos más rentables")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()
