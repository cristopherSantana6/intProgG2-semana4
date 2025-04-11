import random

numero_secreto = random.randint(1, 10)


while(True):
    numero_usuario = int(input("dime el número entre 1 y 10: "))
    if(numero_secreto == numero_usuario): 
        print("felicidades, adivinaste el número secreto: ", numero_secreto)
        break
    else:
        print("sigue intentando")
    if (numero_usuario > numero_secreto):
        print("el número es menor")
    else:
        print("el número es mayor")