carros = ["crossfox", "passat"]
valores = [88054, 56655]

indise = carros.index("passat")
print(indise)

valores[carros.index("crossfox")]

# Esto es un dicciónario
datos = {"jetta variant": 65645, "passat": 6566, "crossfox": 6546546}


# Creando diccionarios con zip()
print(list(zip(carros, valores)))

datos = dict(zip(carros, valores))
print(datos)
