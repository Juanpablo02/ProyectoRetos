def rectangulo():
    anchoo = int(input("Digite el ancho del rectangulo: "))
    largo = int(input("Digite el largo del rectangulo: "))
    area = anchoo * largo
    perimetro= (anchoo * 2) +(largo * 2)
    while largo > 0:
        ancho = anchoo
        while ancho > 0:
            print("*"*ancho)
            ancho = 0
        largo = largo -1
    print(f'Area: {area}')
    print(f'Perimetro:{perimetro}')
    
rectangulo()            