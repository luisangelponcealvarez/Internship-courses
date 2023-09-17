# Mi primera función

nombre = "Luis angel ponce"
edad = 19

print("Este es el texto sin función El nombre es Luis angel y su edad es 19 años")

print(f"El nombre es {nombre} y su edad es {edad} años")

# Esta es una función para pedirle al usuario su nombre
print("Esta es una función")

# la palabra 'def' es una función


def saludar():
    nombre = input("Digite su nombre: ")
    print(f"Hola {nombre} sea bienvenid@!!!")


saludar()