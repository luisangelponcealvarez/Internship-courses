# Esto es un dicciónario
datos = {"jetta variant": 65645, "passat": 6566, "crossfox": 6546546}

print(datos)
# Esto es para autualizar un dato
datos.update({"passat": 565165})

print(datos)
# Esto es para autualizar y para añadir un dato nuevo
datos.update({"passat": 565167, "fusca": 150000})

print(datos)

# Esto es para copiar un diccionario
datosCopy = datos.copy()
print(datosCopy)

# Eliminando un dato de la variable copy
del datosCopy["fusca"]
print(datosCopy)
# El diccionario principal se que da igual solo se modifica el de datosCopy
print(datos)

# dict.pop(key[default])
datosCopy.pop("passat")
datosCopy.pop("passat", "Llave no fue encontrada")
print(datosCopy)
datosCopy.pop("ds5", "llave no fue encontrada")
print(datosCopy)

# dict.clear() este comando borra todo
datosCopy.clear()
print(datosCopy)
