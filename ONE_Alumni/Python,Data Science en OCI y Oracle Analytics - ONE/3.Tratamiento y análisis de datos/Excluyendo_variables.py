import pandas as pd

datos = pd.read_csv('./alquiler_residencial.csv', sep=';')

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

datos_aux = pd.DataFrame(datos[['Tipo Agrupado','Valor m2','Valor Bruto','Valor Bruto m2']])
print(datos_aux.head(10))

# eliminar datos #1
del datos_aux['Valor Bruto']
print(datos_aux.head(10))

# eliminar datos #2
datos_aux.pop('Valor Bruto m2')
print(datos_aux)
 
# eliminar datos #3
# datos.drop(['valor Bruto','Valor Bruto m2'], axis=1,inplace=True)

datos.to_csv('alquiler_residencial.csv',sep=';',index=False)


