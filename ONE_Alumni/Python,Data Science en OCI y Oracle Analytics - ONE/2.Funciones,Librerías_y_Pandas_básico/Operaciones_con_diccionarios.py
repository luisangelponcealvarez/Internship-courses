datos = {"jetta variant": 56546, "passat": 56654, "crossfox": 65646}

print("Este es el dato buscado: ", datos["passat"])

# Esto te da true
print("passat" in datos)

# Esto te da false
print("pass" in datos)

# Esto te da sin no esta el dato teda true
print("fusca" not in datos)

# Esto te da el tamaño del diccionario
print(len(datos))

# Esto agrega un nuevo elemento al diccionario
datos["Ds5"] = 55656
print(datos)

# Esto elimina un dato
del datos["passat"]

print(datos)
