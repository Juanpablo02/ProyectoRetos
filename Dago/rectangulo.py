
#ancho = int(input("Ingresa el ancho del rectangulo: "))
#print(f'El valor del ancho del rectangulo es: {ancho}')
#largo = int(input("Ingresa el largo del rectangulo: "))
#print(f'El valor del largo del rectangulo es: {largo}')

def calcularArea(ancho, largo):
    area = ancho * largo
    print(f'Este es el area del rectangulo: {area}')
calcularArea(5, 5)
def calcularpermimetro(ancho, largo):
    perimetro = (ancho + ancho + largo + largo)
    print(f'El perimetro del rectangulo es: {perimetro}')
calcularpermimetro(5, 5)