""" Realizar la carga del precio de un 
    producto y la cantidad a llevar. 
    Mostrar cuanto se debe pagar 
    (se ingresa un valor entero en el precio del producto)"""

precioProducto = int(input("Ingrese precio producto: "))
cantidadProducto = int(input("Ingrese cantidad a llevar: "))
totalPagar = cantidadProducto * precioProducto
print("El total a pagar es de: " + str(totalPagar))



