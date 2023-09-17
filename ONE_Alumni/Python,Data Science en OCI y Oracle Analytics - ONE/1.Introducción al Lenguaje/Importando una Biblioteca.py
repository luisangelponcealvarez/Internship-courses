#  Importando una Biblioteca
from random import randrange, seed

randrange(0, 11)

notas_matematicas = []
seed(8)
for notas in range(6):
    notas_matematicas.append(randrange(0, 11))
notas_matematicas

len(notas_matematicas)
