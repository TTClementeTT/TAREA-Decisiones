def main():
    # Escribe tu código abajo de esta línea
   a=int(input("ingresa el valor en grados="))
if(a<90 and a>0):
    print("se encuentra en el cuadrante 1")
elif(a==90):
    print("eje")
elif(a>90 and a<180):
    print("se encuentra en el cuadrante 2")   
if(a==180):
    print("eje")
elif(a>180 and a<270):
    print("se encuentra en el cuadrante 3")
if(a==270):
    print("eje")     
elif(a>270 and a<360):
    print("se encuentra en el cuadrante 4")

if(a==360):
    print("eje")
    
elif(a==0):
    print("excede")
elif(a<0):
    print("excede")
elif(a>360):
    print("excede") 
    



if __name__ == '__main__':
    main()
