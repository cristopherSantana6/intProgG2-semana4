#Declara una variable de tipo texto que contenga un número (por ejemplo, "25").
#Luego convierte ese valor a número e imprímelo incrementado en 1.


input_text = input("Introduce un número en formato texto (por ejemplo, '25'): ")
numero = int(input_text)  # Convierte el texto a número entero
numero_incrementado = numero + 1  # Incrementa el número en 1
print("El número incrementado en 1 es:", numero_incrementado)  # Imprime el resultado