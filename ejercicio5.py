#Declara tres variables numéricas y evalúa la siguiente expresión:
#(a + b) * c / 2.
#Muestra el resultado y explica cómo se evalúa la expresión paso a paso

a= int(input("Introduce el valor de la primer variable: "))
b= int(input("Introduce el valor de la segunda variable: "))
c= int(input("Introduce el valor de la tercer variable: "))

resultado= (a + b) * c / 2
print("El resultado de la expresión es: ", resultado)
print("La expresión se evalúa de la siguiente manera: ")
print("1. Se suman las variables a y b.")
print("2. El resultado de la suma se multiplica por la variable c.")
print("3. El resultado de la multiplicación se divide entre 2.")
print("4. El resultado final se muestra en pantalla.")