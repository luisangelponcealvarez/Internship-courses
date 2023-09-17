# Listas
edades = [20, 15, 12, 45, 50]
# Este es el indise
# [20,15,12,45,50]
#   0  1  2  3  4
edades[1]
edades[0:3]
edades[:]
edades[1:]
# Este es el indise
# [20,15,12,45,50]
#   0 -4 -3 -2 -1
edades[-3]

# Lista con diferentes tipos de datos
persona = ["Mariana", 25, True, "México"]

for elemento in persona:
    print(f"El elemento {elemento} de la lista es del tipo ", type(elemento))
