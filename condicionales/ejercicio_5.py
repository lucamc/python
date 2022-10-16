"""De un operario se conoce su sueldo y los años de antigüedad. 
   Se pide confeccionar un programa que lea los datos de entrada e 
   informe:

a) Si el sueldo es inferior a 500 y su antigüedad es igual o 
superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.

b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, 
otorgarle un aumento de 5 %.

c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios. """


sueldo = float(input("Ingrese el sueldo: "))
aniosAniguedad = float(input("Ingrese la antiguedad: "))

if(sueldo < 500 and aniosAniguedad >= 10):
    aumento = sueldo * 0.2
    sueldo += aumento
    print("Tiene un aumento de 20%, sueldo: " + str(sueldo))
else:
    if(sueldo < 500):
        aumento = sueldo * 0.05
        sueldo += aumento
        print("Tiene un aumento de 5%, sueldo: " + str(sueldo))
    else:
        print("El sueldo no tiene aumentos, sueldo: " + str(sueldo))
