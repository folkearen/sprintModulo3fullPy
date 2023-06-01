# SPRINT DE ENTREGA:
# Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:

# ● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).

# ● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.

# ● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.

# ● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
# ● Por cada cuenta debe pedir un número telefónico para contactarse.


# ● El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.
# ● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
# ● Se debe guardar como un string.

# A modo de entrega, se debe disponer un documento Word o PDF en el que se indique: Ruta del repositorio en GitHub

# Consideraciones adicionales
# - El código debe estar debidamente indentado
# - El formato del documento Word queda a criterio del equipo.


import random


def crearContrasenia(name):
    print(f"Se ha creado la contraseña para {name}.")
    aprobarContrasenia = False

    while not aprobarContrasenia:
        mayusculas = "abcdefghijklmnopqrstuvwxyz"
        minusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"
        contrasenia = ''
        for i in range(11):
            ma = random.choice(mayusculas)
            mi = random.choice(minusculas)
            num = random.choice(numeros)
            caracteres = [ma, mi, num]
            caracter = random.choice(caracteres)
            contrasenia += caracter
        aprobarContrasenia = True
            
    return contrasenia
    

def asignarTelefono(name):
    longitud = False
    while not longitud:
        telefono = input(f"Ingrese su número telefónico {name}, recuerde que debe poseer 8 dígitos: ")
        if len(telefono) == 8:
            print('Número telefónico registrado')
            longitud = True
        else:
            print('El número no cumple el requisito de 8 dígitos, por favor vuelva a intentarlo')
    return telefono
def crearCuenta():
    for nombre in nombres:
        nombreUsuario = 'user' + str(len(list(usuarios.keys()))) 
        usuarios[nombreUsuario] = {
            'nombre' : nombre,
            'contrasenia' : crearContrasenia(nombre),
            'telefono' : asignarTelefono(nombre)
        }

nombres = [
    "Martín Sebastián López García",
    "Valentina Sofía Torres Mendoza",
    "Lucas Alejandro Ramírez Vargas",
    "Isabella Victoria Ruiz Blanco",
    "Diego Eduardo Silva Rodríguez",
    "Emilia Antonella Castro Rojas",
    "Matías Daniel Sánchez Morales",
    "Natalia Gabriela Fernández Pérez",
    "Santiago Andrés Morales Herrera",
    "Renata Mariana González Jiménez",
    "Fernanda Magdalena Rojas Flores"
]
usuarios = {

}

crearCuenta()

print(usuarios)