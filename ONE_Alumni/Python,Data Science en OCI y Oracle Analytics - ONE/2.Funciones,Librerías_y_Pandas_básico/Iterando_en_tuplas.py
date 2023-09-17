# Iterando en tuplas
nombres_carros = ("jetta variant", "passat", "crossfox", "ds5")
nombres_carros

for item in nombres_carros:
    print(item)

# Desempacando tuplas
nombres_carros = ("luis", "passat", "crossfox", "ds5")
nombres_carros

carro_1, carro_2, carro_3, carro_4 = nombres_carros

print(carro_1)
print(carro_2)

# Ignorando elementos con _
_, A, _, B = nombres_carros

print(A)
print(B)

# Ignorando elementos cuando tienes muchos elementos
_, A, *_ = nombres_carros

print(A)

# Zip()
carros = ["Jetta variant", "passat", "crossfox", "ds5"]

valores = [55156, 5546, 5565, 6654]

print(list(zip(carros, valores)))

for item in zip(carros, valores):
    print(item)

for carro, valor in zip(carros, valores):
    print(carro, valor)

print("Estos son los valores que cuestan 1000 o mayor")
for carro, valor in zip(carros, valores):
    if valor > 1000:
        print(carro, valor)
