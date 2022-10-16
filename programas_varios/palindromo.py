from functools import partial



#Función verifica si una palabra es Palindromo
def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower() #COnvierto la palabra en minusculas
    palabraInvertida = palabra[::-1] #Aquí genero palabra invertida
    if (palabra == palabraInvertida):
        return True
    else:
        return False


#Funcion Principal que se va ejecutar
def main():
    palabra = input("Ingrese una palabra: ")
    esPalindromo = palindromo(palabra)
    if(esPalindromo):
        print("Es palindromo")
    else:
        print("No es palindromo")


#Punto de entrada de un programa en python
if __name__=='__main__':
    main() #Ejecuto mi funcion principal, main()