""" 🧮 Proyecto 1: Calculadora simple (nivel básico)

Objetivo: practicar variables, condicionales y funciones.
Requisitos:

Pide dos números al usuario.

Permite elegir una operación: suma, resta, multiplicación o división.

Usa funciones para cada operación.

Controla errores con try/except (por ejemplo, división entre cero).

📦 Extra: añade la opción de repetir el cálculo hasta que el usuario decida salir. """
#Funciones
def sumar(valor1,valor2):
    return valor1+valor2
def restar(valor1,valor2):
    return valor1-valor2
def multiplicar(valor1,valor2):
    return valor1*valor2
def dividir(dividendo,divisor):
    return ((dividendo/divisor),(dividendo%divisor))

#Main
eleccion=0
while eleccion != 5 :
    try:
        print("Elige:\n1. sumar\n2. restar\n3. multiplicar\n4. dividir\n5. salir")
        eleccion = int(input("elige una opcion: "))
        match eleccion:
            case 1:
                print("has elegido suma") 
                valor1 = float(input("Escribe el primer valor: "))
                valor2 = float(input("Escribe el segundo valor: "))
                resultado = sumar(valor1,valor2)
                print(resultado)
            case 2:
                print("has elegido rest") 
                valor1 = float(input("Escribe el primer valor: "))
                valor2 = float(input("Escribe el segundo valor: "))
                resultado = restar(valor1,valor2)
                print(resultado)
            case 3:
                print("has elegido multiplicacion") 
                valor1 = float(input("Escribe el primer valor: "))
                valor2 = float(input("Escribe el segundo valor: "))
                resultado = multiplicar(valor1,valor2)
                print(resultado)
            case 4:
                print("has elegido division") 
                dividendo = float(input("Escribe el dividendo valor: "))
                divisor = float(input("Escribe el divisor valor: "))
                resultado = dividir(dividendo,divisor)
                for j,i in enumerate(resultado):
                    if j == 0:
                        print("cociente " + str(i))
                    elif j==1:
                        print("resto " + str(i))
                        
            case 5:
                print("Hasta la proxima")
            case _:
                print("opcion no valida")
    except ValueError:
        print("debes introducir un numero entero")
    except ZeroDivisionError:
        print("no se puede dividir por 0")


