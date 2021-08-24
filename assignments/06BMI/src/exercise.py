def main():
   from math import *
    #escribe tu código abajo de esta línea
    
peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))
imc= ((peso)/(altura)**2)
print("Tu masa corporal es: ",imc)
if(imc<5):
    print("ERROR! REVISA TUS DATOS")
if(imc<20):
    print("Peso bajo")
if(20<=imc<25):
    print("Peso Normal")
if(25<=imc<30):
    print("SobrePeso")
if(30<=imc<40):
    print("Obesidad")
if(imc>=40):
    print("Obesidad Morbida")
  

if __name__=='__main__':
    main()
