"""Se ingresan por teclado tres números, 
si todos los valores ingresados son menores a 10, 
imprimir en pantalla la leyenda 
"Todos los números son menores a diez"."""

num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))
num3 = float(input("Ingrese el número 3: "))

if(num1 < 10 and num2 < 10 and num3 < 10):
    print("Todos los números ingresados son menores a 10")
else:
    print("Hay números que son iguales o mayores a 10")