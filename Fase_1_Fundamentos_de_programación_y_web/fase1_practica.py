# ===========================================
#     💪 EJERCICIOS FASE 1 - PYTHON BÁSICO
# ===========================================

# 🐍 VARIABLES Y TIPOS DE DATOS -----------------------
print("🐍 VARIABLES Y TIPOS DE DATOS -----------------------")
# 1️⃣ Crea 3 variables (nombre, edad, ciudad) y muestra un mensaje con ellas.
# Escribe tu código aquí 👇
nombre = "alex"
edad = 28
ciudad = "madrid"
print(f" mi nombre es {nombre} tengo {edad} años de edad y vivo en {ciudad} ")
# 2️⃣ Declara dos números y muestra su suma, resta, multiplicación y división.
# Escribe tu código aquí 👇
numero1= int(input("escribe un numero: "))
numero2= int(input("escribe otro numero: "))
print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)

# 3️⃣ Convierte una temperatura de Celsius a Fahrenheit (usa fórmula).
# Escribe tu código aquí 👇
celsius = float(input("escribe la temperatura en celsius: "))
fahrenheit =(celsius*9/5)+32
print("la temperatura en fahrenheit es: ",fahrenheit)


# ⚡ CONDICIONALES -----------------------------------
print("⚡ CONDICIONALES -----------------------------------")

# 4️⃣ Pide al usuario un número y di si es positivo, negativo o cero.
# Escribe tu código aquí 👇
numero = int(input("dame un numero y te digo si es positivo, negatico o cero "))
if numero == 0:
    print("el numero es cero")
elif numero > 0:
    print("el numero es positivo")
else:
    print("el numero es negativo")
# 5️⃣ Pide dos números y muestra cuál es mayor (o si son iguales).
# Escribe tu código aquí 👇
numero1 = int(input("escribe el primer numero "))
numero2 = int(input("escribe el numero con el que comparar el anterior "))

if numero1 == numero2:
    print("son iguales")
elif numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
else:
    print(f"{numero2} es mayor que {numero1}")
# 6️⃣ Pide una nota (0 a 10) y muestra si es “Suspenso”, “Aprobado”, “Notable” o “Sobresaliente”.
# Escribe tu código aquí 👇
numero = float(input("escribe la nota que el alumno ha tenido: "))
match numero:
    case _ if numero >= 9:
        print("el alumno ha sacado sobresaliente")
    case _ if numero >= 7:
        print("el alumno ha sacado notable")
    case _ if numero >= 5:
        print("el alumno ha sacado aprobado")
    case _ if numero > 5:
        print("el alumno ha suspendido")
        
        


# 🔁 BUCLES -------------------------------------------
print(" 🔁 BUCLES -------------------------------------------")

# 7️⃣ Muestra todos los números del 1 al 20.
# Escribe tu código aquí 👇
print("los numeros del 1 al 20 son: ")
for i in range (1,21,+1):
    print(i)


# 8️⃣ Muestra solo los números pares entre 1 y 50.
# Escribe tu código aquí 👇
print("los numeros pares entre el 1 y el 50 son: ")
i=1
while i<=50:
    if i % 2 == 0:
        print(i)
    i+=1


# 9️⃣ Calcula la suma de todos los números del 1 al 100.
# Escribe tu código aquí 👇
print("escribe la suma de todos los numeros del 1 al 100")
i=0
contador = 0
while i<100:
    i+=1
    contador = contador + i
    print(f"esto es i {i}")
    print(f"esto es contador {contador}")
print(f"la suma de todos los numeros es {contador}")

# 🔟 Pide un número y muestra su tabla de multiplicar (1 al 10).
# Escribe tu código aquí 👇
numero = int(input("de que numero quieres que te muestre la tabla de multiplicar: "))
for i in range(11):
    print(f"{numero}X{i}={numero*i}")

# 1️⃣1️⃣ Usa un while para contar del 10 al 0 (descendente).
# Escribe tu código aquí 👇
numero=10
while numero>=0:
    print(numero)
    numero-=1

# 🍎 LISTAS -------------------------------------------
print("🍎 LISTAS -------------------------------------------")

# 1️⃣2️⃣ Crea una lista con 5 frutas y muestra cada una con un for.
# Escribe tu código aquí 👇
listaFrutas = ["manzana","platano","cereza","higo","sandia"]
for fruta in listaFrutas:
    print(fruta)

# 1️⃣3️⃣ Agrega una fruta nueva a la lista anterior y muestra el total.
# Escribe tu código aquí 👇
listaFrutas.append("melon")
print(listaFrutas)

# 1️⃣4️⃣ Pide al usuario una fruta y di si está en la lista o no.
# Escribe tu código aquí 👇
pideFruta = input("que fruta desa buscar? ").lower()
contador = 0
for frutas in listaFrutas:
    if pideFruta == frutas:
        print(f"tu fruta esta en la lista es {frutas}")
        contador +=1
if contador == 0:
    print(f"la fruta {pideFruta} no esta en la lista")

# 1️⃣5️⃣ Crea una lista de números y muestra el número mayor y menor.
# Escribe tu código aquí 👇
listaNumeros = [2,5,3,4,4,8,9,1,7,8,6]
numeroMayor=0
numeroMenor=9
for numeros in listaNumeros:
    if numeros >= numeroMayor:
        numeroMayor = numeros
    if numeros <=numeroMenor:
        numeroMenor = numeros
print(f"el mayor numero es {numeroMayor} y el menor es {numeroMenor}")

# 🔧 FUNCIONES ----------------------------------------

# 1️⃣6️⃣ Crea una función que reciba un nombre y lo salude.
# Escribe tu código aquí 👇
def saludar(nombre):
    return f"hola {nombre}"
mensaje = saludar("alex")
print(mensaje)

# 1️⃣7️⃣ Crea una función que calcule el cuadrado de un número.
# Escribe tu código aquí 👇
def cuadradoNumero(numero):
    return int(numero) * int(numero)

resultado = cuadradoNumero(input("escribe un numero: "))
print(resultado)

# 1️⃣8️⃣ Crea una función que reciba dos números y devuelva su promedio.
# Escribe tu código aquí 👇
def promedio(numero1, numero2):
    return (int(numero1)+int(numero2))/2

resultado  = promedio(input("escribe el primer numero "),input("escribe el segundo numero "))
print("el promedio es: "+str(resultado))

# 1️⃣9️⃣ Crea una función que reciba una lista de números y devuelva su suma total.
# Escribe tu código aquí 👇
def sumaTotal(listaNumeros):
    sumatoria = 0
    for numeros in listaNumeros:
        sumatoria = sumatoria + numeros
    return sumatoria

sumatoriaTotal = sumaTotal(listaNumeros = [2,3,5,8])
print(sumatoriaTotal)

# ⚠️ TRY / EXCEPT ------------------------------------

# 2️⃣0️⃣ Pide un número al usuario y usa try/except para evitar errores si escribe texto.
# Escribe tu código aquí 👇
try:
    numero = int(input("ingresa un numero: "))
except ValueError:
    print("Debes introducir un numero entero")
else:
    print(f"el numero que has escrito es {numero} y es de tipo {type(numero).__name__}")

# 🍊 TUPLAS -------------------------------------------
print("🍊 TUPLAS -------------------------------------------")

# 2️⃣1️⃣ Crea una tupla con tres colores y muestra cada uno.
# Escribe tu código aquí 👇
tupla = ("rojo","verde","azul")
print(tupla)
for color in tupla:
    print(color)

# 2️⃣2️⃣ Desempaqueta una tupla con tres números en variables a, b, c y muéstralas.
# Escribe tu código aquí 👇
tuplaNumeros = (1,2,3)
a,b,c = tuplaNumeros
print(a,b,c)

# 2️⃣3️⃣ Convierte una tupla en lista, agrega un elemento nuevo y vuelve a convertirla en tupla.
# Escribe tu código aquí 👇
tuplaLista = list(tupla)
tuplaLista.append("negro")
listaTupla = tuple(tuplaLista)
print(listaTupla)

# 🗝️ DICCIONARIOS ------------------------------------
print("🗝️ DICCIONARIOS ------------------------------------")

# 2️⃣4️⃣ Crea un diccionario con datos de una persona (nombre, edad, ciudad) y muéstralo.
# Escribe tu código aquí 👇
diccionarioPersona = {"nombre":"alex","edad":"28","ciudad":"madrid"}
print(diccionarioPersona)

# 2️⃣5️⃣ Muestra solo las claves del diccionario anterior.
# Escribe tu código aquí 👇
print(diccionarioPersona.keys())

# 2️⃣6️⃣ Muestra solo los valores del diccionario anterior.
# Escribe tu código aquí 👇
print(diccionarioPersona.values())


# 2️⃣7️⃣ Agrega una nueva clave “profesión” al diccionario y muéstralo.
# Escribe tu código aquí 👇
diccionarioPersona["profesion"] = "programador"
print(diccionarioPersona.keys())

# 2️⃣8️⃣ Recorre el diccionario mostrando “clave: valor” en cada línea.
# Escribe tu código aquí 👇
print(diccionarioPersona.items())
for clave, valor in diccionarioPersona.items():
    print(clave,valor)