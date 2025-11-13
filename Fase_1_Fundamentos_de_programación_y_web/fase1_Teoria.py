# ==================================================
#                    🚀 FASE 1 - FUNDAMENTOS PYTHON
# ==================================================

# ==================================================
#                         ÍNDICE
# ==================================================
# 1️⃣ VARIABLES Y TIPOS
# 2️⃣ OPERADORES
# 3️⃣ ESTRUCTURAS DE CONTROL
# 4️⃣ MATCH-CASE (similar a switch)
# 5️⃣ FUNCIONES
# 6️⃣ LISTAS
# 7️⃣ TUPLAS
# 8️⃣ DICCIONARIOS
# 9️⃣ INPUT Y CONVERSIÓN
# 🔟 MANEJO DE ERRORES CON TRY/EXCEPT
# 1️⃣1️⃣ TIPOS DE ERRORES COMUNES EN PYTHON
# 1️⃣2️⃣ ATRIBUTOS Y MÉTODOS MÁGICOS (DUNDER)
# 1️⃣3️⃣ CONDICIONALES Y TERNARIO
# 1️⃣4️⃣ BUCLES Y MÉTODOS DE RECORRIDO

# ==================================================
# 1️⃣ VARIABLES Y TIPOS
# ==================================================
# Almacenan datos: int, float, str, bool, list, dict

# ==================================================
# 2️⃣ OPERADORES
# ==================================================
# Aritméticos: +, -, *, /, //, %, **
# Comparación: ==, !=, >, <, >=, <=
# Lógicos: and, or, not
# Asignación: =, +=, -=, *=, /=, etc.
# Pertenencia: in, not in
# Identidad: is, is not

# ==================================================
# 3️⃣ ESTRUCTURAS DE CONTROL
# ==================================================
# if, elif, else → decisiones
# for, while → bucles

# ==================================================
# 4️⃣ MATCH-CASE (similar a switch)
# ==================================================
# match variable:
#     case valor1:
#         ...
#     case valor2:
#         ...
#     case _:
#         ...  # caso por defecto

# ==================================================
# 5️⃣ FUNCIONES
# ==================================================
# def nombre_funcion(parametros):
#     ... 
#     return valor

# ==================================================
# 6️⃣ LISTAS
# ==================================================
# Crear: lista = [elem1, elem2]
# Acceder: lista[0], lista[-1]
# Agregar:
#   append(elem) → añade al final
#   insert(pos, elem) → añade en una posición específica
# Eliminar:
#   pop(pos) → elimina y devuelve un elemento (último por defecto)
#   remove(valor) → elimina la primera aparición de ese valor
# Tamaño: len(lista)
# Recorrer:
#   for elem in lista: ... → recorre directamente los valores
#   for i in range(len(lista)): ... → recorre por índice
#   for i, elem in enumerate(lista): ... → recorre índice y valor a la vez

# ==================================================
# 7️⃣ TUPLAS
# ==================================================
# Inmutables (no se pueden modificar)
# Crear: tupla = (elem1, elem2)
# Acceder: tupla[0]
# Desempaquetar: a, b = tupla
# Convertir a lista: list(tupla)
# Ejemplo con enumerate:
tupla = ("rojo", "verde", "azul")
for i, color in enumerate(tupla):
    print(i, color)

# ==================================================
# 8️⃣ DICCIONARIOS
# ==================================================
# Pares clave:valor
# Crear: dic = {"nombre": "Ana", "edad": 20}
# Acceder: dic["nombre"]
# Agregar/Modificar: dic["clave"] = valor
# Eliminar: del dic["clave"]
# Métodos útiles:
#   keys() → devuelve las claves
#   values() → devuelve los valores
#   items() → devuelve pares (clave, valor)
# Recorrer:
#   for clave, valor in dic.items(): ...

# ==================================================
# 9️⃣ INPUT Y CONVERSIÓN
# ==================================================
# input() → str
# int(input()), float(input()) → convertir

# ==================================================
# 🔟 MANEJO DE ERRORES CON TRY/EXCEPT
# ==================================================
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Debes introducir un número entero")
except Exception as e:
    print("Ocurrió un error:", e)
else:
    print(f"El número que has escrito es {numero} y es de tipo {type(numero).__name__}")
finally:
    print("Fin del bloque try/except")

# Ejemplo más completo con múltiples errores
try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    resultado = a / b
except ValueError:
    print("Debes introducir un número entero")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except Exception as e:
    print("Error inesperado:", e)
else:
    print("Resultado:", resultado)
finally:
    print("Operación finalizada")

# Lanzar errores manualmente
edad = int(input("Escribe tu edad: "))
if edad < 0:
    raise ValueError("La edad no puede ser negativa")  

# ==================================================
# 1️⃣1️⃣ TIPOS DE ERRORES COMUNES EN PYTHON
# ==================================================
# | Error               | Descripción                                      | Ejemplo                             |
# |--------------------|-------------------------------------------------|-------------------------------------|
# | SyntaxError         | Código con sintaxis incorrecta                  | print("Hola mundo"                  |
# | NameError           | Variable no definida                            | print(x)                             |
# | TypeError           | Operación con tipo incorrecto                   | "2" + 2                              |
# | ValueError          | Valor inválido para la operación                | int("hola")                          |
# | IndexError          | Índice fuera de rango                            | lista = [1,2]; lista[5]             |
# | KeyError            | Clave inexistente en diccionario                | dic = {"nombre":"Ana"}; dic["edad"] |
# | ZeroDivisionError   | División entre cero                              | 5 / 0                                |
# | AttributeError      | Atributo o método inexistente en objeto         | "hola".push("mundo")                 |
# | ImportError         | Módulo no encontrado                             | import modulo_inexistente            |
# | Exception           | Error genérico (captura cualquier otro)        | try: ... except Exception as e: ...  |

# ==================================================
# 1️⃣2️⃣ ATRIBUTOS Y MÉTODOS MÁGICOS (DUNDER)
# ==================================================
# | Atributo / Método | Qué hace | Ejemplo |
# |------------------|---------|---------|
# | __class__        | Clase del objeto | 5.__class__ → <class 'int'> |
# | __name__         | Nombre de la clase (usado con type()) | type(5).__name__ → 'int' |
# | __doc__          | Documentación de la clase | int.__doc__ |
# | __str__()        | Representación amigable | 5.__str__() → '5' |
# | __repr__()       | Representación oficial | 5.__repr__() → '5' |
# | __len__()        | Longitud | "hola".__len__() → 4 |
# | __getitem__()    | Acceso por índice o clave | [1,2,3].__getitem__(1) → 2 |
# | __setitem__()    | Asignar valor por índice o clave | lista.__setitem__(0,5) |
# | __delitem__()    | Eliminar elemento | lista.__delitem__(0) |
# | __iter__()       | Devuelve un iterador | iter([1,2,3]).__iter__() |
# | __next__()       | Siguiente de iterador | i = iter([1,2,3]); i.__next__() → 1 |
# | __eq__(), __lt__(), __gt__() | Comparaciones | 5.__eq__(5) → True |
# | __add__(), __mul__() | Operaciones aritméticas | (2).__add__(3) → 5 |
# | __contains__()   | Verifica pertenencia | [1,2,3].__contains__(3) → True |

# ==================================================
# 1️⃣3️⃣ CONDICIONALES Y TERNARIO
# ==================================================
# if condicion:
#     ...
# elif otra_cond:
#     ...
# else:
#     ...
# Ternario: resultado = valor_si_true if condicion else valor_si_false

# ==================================================
# 1️⃣4️⃣ BUCLES Y MÉTODOS DE RECORRIDO
# ==================================================
# Formas de recorrer listas, tuplas, diccionarios y otros iterables:

# a) Recorriendo directamente valores
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

# b) Recorriendo por índice
for i in range(len(colores)):
    print(i, colores[i])

# c) Recorriendo índice + valor
for i, color in enumerate(colores):
    print(i, color)

# d) Recorriendo varios iterables a la vez
nombres = ["Ana", "Luis", "Marta"]
edades = [20, 25, 22]
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

# e) Recorriendo diccionarios
dic = {"nombre": "Ana", "edad": 20}
for clave, valor in dic.items():
    print(clave, valor)
for clave in dic.keys():
    print(clave)
for valor in dic.values():
    print(valor)

# f) Recorriendo al revés
for color in reversed(colores):
    print(color)

# g) Recorriendo en orden ascendente
numeros = [3, 1, 4, 2]
for n in sorted(numeros):
    print(n)

# h) Bucles con control de flujo
for i in range(10):
    if i == 3:
        continue  # Salta esta iteración
    if i == 7:
        break     # Sale del bucle
    print(i)

# Ejemplo de bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
