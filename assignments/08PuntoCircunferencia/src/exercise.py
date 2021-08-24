import math

def main():
    # Escribe tu código abajo de esta línea
    from math import sqrt
radio= float(input("Dame el radio="))
coordenadax1= float(input("X1 Coordenada x del centro de la circunferencia="))
coordenaday1= float(input("Y1 Coordenada y del centro de la circunferencia="))
coordenadax2punto= float(input("X2 Coordenada x del punto="))
coordenaday2punto= float(input("Y2 Coordenada y del punto="))

distancia= sqrt((coordenadax2punto-coordenadax1)**2 + (coordenaday2punto-coordenaday1)**2)

if distancia<radio:
    print("DENTRO")
elif distancia==radio:
    print("SOBRE")
else:
    print("FUERA")
    


if __name__ == '__main__':
    main()
