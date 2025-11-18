# 4️⃣ Mini juego: Piedra, papel o tijera

# Jugador vs. ordenador

# Lógica para decidir ganador

# Validación de inputs

# Uso del módulo random

#importamos random

import random

def obtener_maximo_filas_columnas(tablero):
    maximo_filas = [len(tablero)]
    maximo_columnas = [len(fila) for fila in tablero]
    return [maximo_filas[0]-1,maximo_columnas[0]-1]

def seleccionar_casilla(eleccion_fila,eleccion_columna,tablero,filas_y_columnas,turno):
    if turno % 2 == 1:
        eleccion_fila = int(input(f"indica una fila comprendida entre 0 y {filas_y_columnas[0]}: "))
        eleccion_columna = int(input(f"indica una columna comprendida entre 0 y {filas_y_columnas[1]}: "))
        while (eleccion_fila > filas_y_columnas[0] or eleccion_columna > filas_y_columnas[1]) or (tablero[eleccion_fila][eleccion_columna]=="x" or tablero[eleccion_fila][eleccion_columna]=="o"):
            print("casilla ya dibujada o numero de fila/columna invalido")
            eleccion_fila = int(input(f"indica una fila comprendida entre 0 y {filas_y_columnas[0]}: "))
            eleccion_columna = int(input(f"indica una columna comprendida entre 0 y {filas_y_columnas[1]}: "))
    else:
        while tablero[eleccion_fila][eleccion_columna]=="x" or tablero[eleccion_fila][eleccion_columna]=="o":
            eleccion_fila = random.randint(0,filas_y_columnas[0])
            eleccion_columna = random.randint(0,filas_y_columnas[1])
    return eleccion_fila,eleccion_columna

def imprimir_valor(tablero):
    for valores in tablero:
        print(valores)

def turnometro(turno):
    print("estamos en el turno:",turno)
    if turno % 2 == 0:
        print("Turno de la CPU: ")
    else:
        print("Turno del USUARIO: ")
    turno+=1
        
    return turno

def condicion_finalizar_partida(turno):
    if turno == 10:
        print("se acabo la partida")
        return True
    
    return False
        
    

def main():
    # nombre_jugador1 = input("Por favor indique el nombre del jugador : ")
    tablero = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    turno = 1
    eleccion_fila=0
    eleccion_columna=0
    finalizar=False
    
    while (turno)<10:
        filas_y_columnas = obtener_maximo_filas_columnas(tablero)

        
        resultado = seleccionar_casilla(eleccion_fila,eleccion_columna,tablero,filas_y_columnas,turno)
        eleccion_fila = resultado[0]
        eleccion_columna = resultado[1]

        turno = turnometro(turno)
        
        for indices,valores in enumerate(tablero):
            for posicion in valores:
                tablero[eleccion_fila][eleccion_columna]="x"
        imprimir_valor(tablero)
        
        finalizar = condicion_finalizar_partida(turno)
        if finalizar == True:
            break
        
        resultado = seleccionar_casilla(eleccion_fila,eleccion_columna,tablero,filas_y_columnas,turno)
        eleccion_fila = resultado[0]
        eleccion_columna = resultado[1]
        
        turno = turnometro(turno)
        
        
        for indices,valores in enumerate(tablero):
            for posicion in valores:
                tablero[eleccion_fila][eleccion_columna]="o"
        imprimir_valor(tablero)

        finalizar = condicion_finalizar_partida(turno)
        if finalizar == True:
            break
        



if __name__ == "__main__":
    main()