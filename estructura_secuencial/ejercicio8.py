""" Calcular el sueldo mensual de un 
    operario conociendo la cantidad de horas
    trabajadas y el valor por hora. """


cantidadHoras = float(input("Ingrese cantidad de horas trabajadas: "))
valorHora = float(input("Ingrese el valor por hora trabajada: "))
sueldo = cantidadHoras * valorHora
print("EL sueldo mensual del operario es de: " + str(sueldo))
