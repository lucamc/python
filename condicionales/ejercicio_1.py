"""Confeccionar un programa que lea 
por teclado tres números enteros distintos y 
nos muestre el mayor."""

num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))
num3 = float(input("Ingrese número 3: "))

if(num1 > num2 and num1 > num3):
    print("El número maoyor es el: " + str(num1))
else:
    if(num2 > num3):
        print("El número mayor es el: " + str(num2))
    else:
        print("El número mayor es el: " + str(num3))