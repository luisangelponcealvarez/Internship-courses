# Ciclos y Bucles

# Bucle fuera de la función
edades = [20, 15, 12, 45, 50]


def verificar_si_puede_conducir_sin_parametro():
    if edad >= 18:
        print("Usted tiene edad suficiente para conducir")
    else:
        print("Usted No tiene edad suficiente para conducir")


for edad in edades:
    verificar_si_puede_conducir_sin_parametro()


# Bucle dentro de la función
edades = [20, 15, 12, 45, 50]


def verificar_si_puede_conducir_sin_parametro_con_bucle(edades):
    for edad in edades:
        if edad >= 18:
            print("Usted tiene edad suficiente para conducir")
        else:
            print("Usted No tiene edad suficiente para conducir")

    verificar_si_puede_conducir_sin_parametro(edades)
