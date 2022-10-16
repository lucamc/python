#Conversor de Monedas

#Funcion conversor
def conversorMoneda(tipoMoneda, valorDolar):
    pesos = float(input("Ingresa cantidad de " + tipoMoneda + ": "))
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + (dolares) + " dolares")


#Menu de opciones de Monedas DIsponibles
menu = """

Conversor de Monedas

1 - Pesos Uruguayos
2 - Pesos Argentinos
3 - Reales

Elige una ocpion: """


#Capturo por teclado el tipo de Moneda
opcion = int(input(menu))



#Valido que tipo de moneda realizar la conversion
if(opcion == 1):
    conversorMoneda("Pesos URU", 41.44)

elif(opcion == 2 ):
    conversorMoneda("Pesos ARG", 154.44)

elif(opcion == 3):
    conversorMoneda("Reales", 5.33)
else:
    print("Ingresa una opción correcta")
