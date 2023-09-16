import sqlite3
import pandas as pd

square = lambda x: x * x

with sqlite3.connect('Nordthwind.sql') as conn:
    conn.create_function('square', 1, square)
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT * FROM Productk'''
    )
    result = cursor.fetchall()
    result_df = pd.DataFrame(result)

print(result_df)
