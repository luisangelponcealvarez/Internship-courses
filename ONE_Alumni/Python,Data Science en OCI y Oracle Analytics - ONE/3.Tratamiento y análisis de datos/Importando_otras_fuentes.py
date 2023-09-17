import pandas as pd

# Aquí vemos en formato json
json = open("pandas/extras/alquiler.json")
print(json)

# Aquí vemos en formato tabla el json
df_json = pd.read_json("pandas/extras/alquiler.json")
print(df_json)

# Aquí vemos como sacar los datos de un txt
txt = open("pandas/extras/alquiler.txt")
print(txt.read())

# Aquí abrimos un txt con pandas
df_txt = pd.read_table("Pandas/extras/alquiler.txt")
print(df_txt)

# Aquí abrimos un exel
df_xlsx = pd.read_excel("Pandas/extras/alquiler.xlsx")
print(df_xlsx)

# Aquí abrimos un html
df_html = pd.read_html("Pandas/extras/datos_html_1.html")
print(df_html[0])

# Aquí abrimos un pagina web
df_html = pd.read_html("https://librefutboltv.com/")
print(len(df_html[0]))
