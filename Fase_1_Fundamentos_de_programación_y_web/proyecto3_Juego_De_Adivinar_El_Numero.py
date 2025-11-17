# 3️⃣ Juego de adivinar el número PRO con colores y estilo

import random
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

# Función: genera número aleatorio
def generar_numero_aleatorio():
    return random.randint(1, 100)

# Función: muestra pista con colores y estilos
def mostrar_pista(intento, numero_resultado):
    if numero_resultado > intento:
        print(Fore.YELLOW + f"\n🔼 El número es mayor que {intento}")
        return False
    elif numero_resultado < intento:
        print(Fore.CYAN + f"\n🔽 El número es menor que {intento}")
        return False
    else:
        print(Fore.GREEN + Style.BRIGHT + f"\n🎉 ¡Felicidades! Has acertado. El número era {numero_resultado}")
        return True

# Función principal
def main():
    numero_resultado = generar_numero_aleatorio()
    intento = 0
    contador = 0

    print(Fore.MAGENTA + Style.BRIGHT + "="*40)
    print(Fore.MAGENTA + Style.BRIGHT + "      ¡Bienvenido al Juego de Adivinar!")
    print(Fore.MAGENTA + "         Adivina un número del 1 al 100")
    print(Fore.MAGENTA + "="*40 + "\n")

    while True:
        try:
            intento = int(input(Fore.WHITE + "Introduce tu intento: "))

            if intento < 1 or intento > 100:
                print(Fore.RED + "❌ Error: ingresa un número entre 1 y 100")
            else:
                contador += 1
                solucion = mostrar_pista(intento, numero_resultado)
                if solucion:
                    print(Fore.BLUE + Style.BRIGHT + f"\nTotal de intentos: {contador}")
                    print(Fore.MAGENTA + Style.BRIGHT + "="*40)
                    print(Fore.MAGENTA + "          ¡Gracias por jugar!")
                    print(Fore.MAGENTA + "="*40 + "\n")
                    break
        except ValueError:
            print(Fore.RED + "❌ Error: se esperaba un valor entero")
        except Exception as e:
            print(Fore.RED + "⚠️ Error inesperado:", e)
            print(type(e))

if __name__ == "__main__":
    main()
