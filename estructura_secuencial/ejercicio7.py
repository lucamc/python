""" Realizar un programa que lea 
    cuatro valores numéricos e informar 
    su suma y promedio. """



num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print("La suma de todos los números es de: " + str(suma))
print("El promedio de todos los números es de: " + str(promedio))