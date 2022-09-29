
#ancho = int(input("Ingresa el ancho del rectangulo: "))
#print(f'El valor del ancho del rectangulo es: {ancho}')
#largo = int(input("Ingresa el largo del rectangulo: "))
#print(f'El valor del largo del rectangulo es: {largo}')

#def calcularArea(ancho, largo):
#    for i in range(1, largo + 1):
#        for j in range(1, ancho + 1):
#            print("*", end="")
#        print(" ")
#    area = ancho * largo
#    print(f'Este es el area del rectangulo: {area}')
#calcularArea(5, 5)
#
#def calcularPermimetro(ancho, largo):
#    for i in range(1, largo + 1):
#        for j in range(1, ancho + 1):
#            print("*", end="")
#        print(" ")
#    perimetro = (ancho + ancho + largo + largo)
#    print(f'El perimetro del rectangulo es: {perimetro}')
#calcularPermimetro(5, 5)

def calcular (ancho, largo):
    if(ancho <= 10 and largo <= 20):
        area = ancho * largo
        print(f'Este es el area del rectangulo: {area}')
        perimetro = (ancho + ancho + largo + largo)
        print(f'El perimetro del rectangulo es: {perimetro}')
        for i in range(1, largo + 1):
            for j in range(1, ancho + 1):
                print("*", end="")
            print(" ")
    else:
        print("El valor ingresado debe de ser menor a 10(ancho) y menor a 20(largo)")
calcular(5, 3)