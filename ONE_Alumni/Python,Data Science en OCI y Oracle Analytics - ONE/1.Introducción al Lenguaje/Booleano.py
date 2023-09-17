# Booleano
edad = 18
edad >= 18
edad < 18
edad == 18

verificaciones = []
edades = [13, 15, 20]


def verificar_si_puede_conducir_bool(verificaciones, edades):
    for edad in edades:
        if edad >= 18:
            verificaciones.append(True)
        else:
            verificaciones.append(False)
    for verificacion in verificaciones:
        if verificacion == True:
            print("Usted tiene edad suficiente para conducir")
        else:
            print("Usted tiene edad suficiente para conducir")


verificar_si_puede_conducir_bool(verificaciones, edades)
