def login():
    i = True
    contador = 0
    while(i):
        usuario = input("digite el usuario: ")
        contraseña = input("digite la contraseña: ")
        if (usuario == "admin" and contraseña == "admin123"):
            print("Bienvenido")
            i= False
        else:
            contador = contador + 1
            print(f'llevas {contador} intentos')
login()
