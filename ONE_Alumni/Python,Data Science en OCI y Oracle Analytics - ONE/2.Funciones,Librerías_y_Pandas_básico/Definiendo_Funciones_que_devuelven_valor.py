def media(lista):
    valor = sum(lista) / len(lista)
    return (valor, len(lista))


resultado, n = media([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(resultado, n)
