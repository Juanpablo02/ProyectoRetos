
def rectangulo ():

    altura = float (input ('Ingresa el valor de altura: '))
    base = float (input ('Ingresa el valor de base: '))
    area=base*altura
    perimetro=(altura*2)+(base*2)
    print ('Valor de area: ' + repr (area))
    print ('Valor de perimetro: ' + repr (perimetro))
    print ()

rectangulo()

'''
def area_rectangulo(base, altura):
    return base * altura

print("Área de rectángulo: ")
print(area_rectangulo(8, 2))
'''