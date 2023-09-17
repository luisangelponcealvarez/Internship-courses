# Documentación de las Built-in_function
# (https://docs.python.org/3/library/functions.html)

datos = {"jetta variant": 6564, "passat": 1323, "crossfox": 2133}

# listando los valores
valores = []
for valor in datos.values():
    valores.append(valor)

print(valores)

# sumando los valores sin una built-in function
suma = 0
for valor in datos.values():
    suma += valor
print(suma)

# sumando los valores con una built-in funciton
list(datos.values())
sum(datos.values())

# para pedir ayuda o saber que hacen los comandos
help(sum)
