""" 2️⃣ Gestor de listas de la compra

Objetivo: Practicar listas, bucles y entrada de datos.

Descripción:
Crea un programa que permita:

Agregar productos a una lista.

Mostrar todos los productos.

Eliminar un producto específico.

Salir del programa.

Bonus: Asegúrate de que no se repitan productos y muestra mensajes claros al usuario. """

#funciones
#funcion: crea lista de la compra
def crear_lista_compra():
    listaCompra = []
    return listaCompra

#funcion: agrega un solo producto a la lista creada 
def agregar_un_producto(listaCompra):
    print()
    valor = input("escribe el producto que deseas agregar a la lista de la compra: ").lower() #pide un valor para agregar a la lista y lo convierte a minusculas
    #comprueba si ese valor esta ya en la lista
    if valor == "":
        print("no has escrito nada")
    else:
        if valor in listaCompra:
            print("ese producto ya esta en la lista de la compra")
        else:
            print("agregando producto a la lista")
            listaCompra.append(valor)
    print()

#funcion: muestra la lista de productos
def mostrar_productos(listaCompra):
    print()
    if not listaCompra:
        print("la lista esta vacia")
    else:
        print("la lista de la compra contiene:")
        for productos in listaCompra:
                print(productos)
    print()            
#funcion: eliminar un solo producto de la lista creada
def eliminar_un_producto(listaCompra):
    print()
    valor = input("escribe el elemento que desea eliminar: ").lower()#pide un valor para eliminar de la lista y lo convierte a minusculas
    #comprueba si ese valor existe en la lista y de ser asi lo elimina
    if valor in listaCompra:
        print("el valor eliminado es", valor)
        listaCompra.remove(valor)
    else:
        print("el valor no se ha podido eliminar por que esta mal escrito o no esta en la lista")
    print()
        
#main: la funcion principal
def main():
    #crea un diccionario con los metodos a ejecutar y les asigna un indice para poder elegirlos
    opciones = {
        1: agregar_un_producto,
        2: mostrar_productos,
        3: eliminar_un_producto
    }
    eleccion = 0
    listaCompra = crear_lista_compra()
    #bucle: mientras la eleccion no sea 4 (salir) repitete
    while eleccion != 4:
        try:
            #elige la eleccion que deseas mediante un imput
            eleccion = int(input("elige una opcion:\n1.agregar producto\n2.mostrar productos de la lista\n3.borrar producto de la lista\n4.salir\n"))
            #if: si eleccion es 4 sal del programa
            if eleccion == 4:
                print("hasta la proxima")
            #si eleccion(valor dado por el usuario) es cualquiera de las opciones(dicionario de metoodos con indices)
            elif eleccion in opciones:
                opciones[eleccion](listaCompra)#elige la opcion y le pasa la lista como parametro (listacompra)
            #sino pedimos otra opcion
            else:
                print("error elige otra opcion")
        #manejamos los errores por valores incorrectos
        except ValueError:
            print("error:tienes que escribir un numero como por ejemplo 2 y no 'dos'")
        #en caso de que no sea por valor incorrecto uno mas generico
        except Exception as e:
            print("error inexperado, vuelva a intentarlo")
            print(e)
            print(type(e))
            
#__name__ es una variable dunder contiene si es el mismo archivo el valor main y si es importado desde otro archivo el nombre del otro archivo, archivo2.py seria archivo2 el valo, en resumen lo que hace es que si es el mismo archivo se ejecuta main y si es otro no a menos que le llames
if __name__ == "__main__":
    main()