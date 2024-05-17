import random

numero_secreto=random.randint(1,10)
print(numero_secreto)
numero=int(input("Ingrese un numero\n"))
contador= 0
acierto=0

if (numero == numero_secreto):
        print ("Acertaste el numero\n")
else: 
    contador= contador +1
    while (numero != numero_secreto and contador<5):
        numero=int(input("Ingrese otro numero\n"))
        if (numero < numero_secreto): 
            print ("El numero es menor al numero secreto\n")
        else:
            print ("El numero es mayor al numero secreto\n")
        contador= contador +1

if (contador== 5):
     print(f"Perdiste el juego, el numero era: {numero_secreto}")