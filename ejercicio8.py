#Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15% de 200?

numero= int(input("Introduce el número del cual deseas calcular el porcentaje: "))
porcentaje= int(input("Introduce el porcentaje que deseas calcular: ").replace("%", ""))
resultado= (numero * porcentaje) / 100
print("El resultado de ", porcentaje, "% de ", numero, " es: ", resultado)
