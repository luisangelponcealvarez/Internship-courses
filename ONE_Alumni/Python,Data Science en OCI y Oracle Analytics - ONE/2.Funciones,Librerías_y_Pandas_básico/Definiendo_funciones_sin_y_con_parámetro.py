# funciones sin parametros
def media():
    valor = (1 + 2 + 3) / 3
    print(valor)


media()


# funcion con parámetros
def media(number_1, number_2, number_3):
    valor = (number_1 + number_2 + number_3) / 3
    print(valor)


media(1, 6, 6)


# funcion para sumar mejorada
def media(lista):
    valor = sum(lista) / len(lista)
    print(valor)


resultado = media([1, 2, 3, 4, 5, 6, 7, 8])
