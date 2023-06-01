import random
caracteres ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
contrasenia = ''
for i in range(10):
    contrasenia += random.choice(caracteres)

print(contrasenia)