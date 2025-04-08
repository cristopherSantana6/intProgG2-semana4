#Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una variable auxiliar para hacerlo.


variable1 = int(input("Introduce el primer número: "))
variable2 = int(input("Introduce el segundo número: "))

print (f"el numero {variable1} esta en primera posicion")
print (f"el numero {variable2} esta en segunda posicion")

temporal = variable1
variable1 = variable2
variable2 = temporal
print (f"el numero {variable1} esta en primera posicion")
print (f"el numero {variable2} esta en segunda posicion")

