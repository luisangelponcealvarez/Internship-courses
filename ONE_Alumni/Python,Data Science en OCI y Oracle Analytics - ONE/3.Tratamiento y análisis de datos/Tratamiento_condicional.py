import pandas as pd
 
datos = pd.read_csv('./alquiler_residencial.csv', sep=';')
print(datos.head(10))

datosMantenimiento = datos[datos['Mantenimiento'].isnull()].shape[0]
print(datosMantenimiento)

seleccion = (datos['Mantenimiento'].isnull()) & (datos['Tipo'] == 'Departamento')
print(seleccion)

A = datos.shape[0]
datos = datos[~seleccion]
B = datos.shape[0]
print(A - B)

datos = datos.fillna({'Mantenimiento':0,'Impuesto':0})

datosMantenimiento = datos[datos['Mantenimiento'].isnull()].shape[0]
print(datosMantenimiento)

datosMantenimiento = datos[datos['Impuesto'].isnull()].shape[0]
print(datosMantenimiento)

print(datos.info())

datos.to_csv('alquiler_residencial.csv', sep=';',index=False)
