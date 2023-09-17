import pandas as pd 
datos = pd.read_csv('./alquiler_residencial.csv',sep=';')
print(datos.head(10))

datos['Valor Bruto'] = (datos['Valor']) + (datos['Mantenimiento']) + (datos['Impuesto'])
print(datos.head(10))

datos['Valor m2'] = (datos['Valor']) / (datos['Area'])
print(datos.head(10))

datos['Valor m2'] = datos['Valor m2'].round(2)
print(datos.head(10))

datos['Valor Bruto m2'] = ((datos['Valor Bruto']) / (datos['Area'])).round(2)
print(datos.head(10))

casa = ['Casa','Casa en condominio', 'Casa de villa'] 
datos['Tipo Agrupado'] = datos['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Departamento')
print(datos) 