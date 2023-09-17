# Esto es un dicciónario
datos = {"jetta variant": 65645, "passat": 6566, "crossfox": 6546546}

print(datos)

# dict.keys() es para conoser las llaves
print(datos.keys())

for key in datos.keys():
    print(key)

# dict.values() es para conoser los valores
print(datos.values())

# dict.items() este debuelve una tupla este metodo es parecido al zip()
print(datos.items())

for item in datos.items():
    print(item)

# aquí descomprimimos los valores
for key, value in datos.items():
    print(key, "->", value)

# aquí filtramos los datos
print("Estos son los datos filtrados")
for key, value in datos.items():
    if (value) > 10000:
        print(key)
