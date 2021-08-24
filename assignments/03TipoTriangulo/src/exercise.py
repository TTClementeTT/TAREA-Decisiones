def main():
    #escribe tu código abajo de esta línea
  print("todos los numeros son mayores a 0")

valora=int(input("ingresa el valor a="))
valorb=int(input("ingresa el valor b="))
valorc=int(input("ingresa el valor c="))


if(valora+valorb>valorc and valora+valorc>valorb and valorb+valorc>valora):
    print("ES TRIANGULO")
else:
    print("NO ES TRIANGULO")

if(valora==valorb and valora==valorc):
    print("EQUILATERO")

elif(valora!=valorb and valora!=valorc and valorb!=valorc):
    print("ESCALENO")

else:
    print("ISOSCELES")
     




if __name__=='__main__':
    main()
