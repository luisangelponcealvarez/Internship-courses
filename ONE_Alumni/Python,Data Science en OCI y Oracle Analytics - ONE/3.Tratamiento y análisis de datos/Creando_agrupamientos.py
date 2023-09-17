import pandas as pd 
datos = pd.read_csv('alquiler_residencial.csv',sep=';')
print(datos.head(10))

datos['Valor'].mean()

barrios = ['Ate','Barranco','Comas','Lince','El Agustino','San Luis','Callao']
seleccion = datos['Distrito'].isin(barrios)
datos = datos[seleccion]
print(datos.head(10))

datos['Distrito'].drop_duplicates()
print(datos)

grupo_barrio = datos.groupby('Distrito')
print(grupo_barrio)

print(grupo_barrio.groups)

for barrio, data in grupo_barrio:
    print('{} -> {}'.format(barrio, data.Valor.mean()))

print(grupo_barrio[['Valor','Mantenimiento']].mean().round(2))

