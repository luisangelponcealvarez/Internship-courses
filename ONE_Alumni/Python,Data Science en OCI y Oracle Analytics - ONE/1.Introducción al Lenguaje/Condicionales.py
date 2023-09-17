# Condicionales
edad = 18


def verificar_si_puede_conducir(edad):
    if edad >= 18:
        print("Usted tiene edad suficiente para conducir")
    else:
        print("Usted No tiene edad suficiente para conducir")


verificar_si_puede_conducir(edad)


# Condicionales sin parámetro y conversión de tipo de dato
def verificar_si_puede_conducir_sin_parametro():
    edad = input("Digite su edad: ")
    edad = int(edad)
    if edad >= 18:
        print("Usted tiene edad suficiente para conducir")
    else:
        print("Usted No tiene edad suficiente para conducir")


verificar_si_puede_conducir_sin_parametro()
