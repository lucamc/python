"""Se ingresan tres valores por teclado, 
si todos son iguales se imprime la suma del 
primero con el segundo y a este resultado se lo 
multiplica por el tercero."""

num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))
num3 = float(input("Ingrese el número 3: "))

if(num1 == num2 and num1 == num3 and num2 == num3):
    suma = num1 + num2
    print("La suma del num1 con num2 es de: " + str(suma))
    producto = suma * num3
    print("El producto de la suma con el número3 es de: " + str(producto))
else:
    print("Los números no son todos iguales")