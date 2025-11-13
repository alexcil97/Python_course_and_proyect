from collections import OrderedDict

# Diccionario principal con categorías en orden fijo
t1 = OrderedDict({categoria: {} for categoria in [
    "Control de Versiones", "CI/CD", "Cloud Computing", "Lenguajes de Programación",
    "Desarrollo de Interfaces", "APIs y Servicios Web", "Contenedores",
    "Bases de Datos", "Visualización de Datos", "Seguridad", "Testing", "Desarrollo Móvil","Big data y procesamiento de datos"
]})

# Diccionario para guardar a qué categoría pertenece cada tecnología
tech_to_category = {}

def obtener_entero(mensaje):
    """Solicita un número entero y maneja errores de entrada."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número entero.")

def seleccionar_categoria():
    """Muestra las categorías y permite seleccionar una."""
    print("\n📂 Categorías disponibles:")
    for i, cat in enumerate(t1.keys(), 1):
        print(f"{i}. {cat}")

    while True:
        seleccion = obtener_entero("\nElige el número de la categoría: ") - 1
        if 0 <= seleccion < len(t1):
            return list(t1.keys())[seleccion]
        print("❌ Opción inválida. Inténtalo de nuevo.")

def mostrar_datos():
    """Muestra el diccionario estructurado de forma más legible manteniendo el orden."""
    print("\n📊 **Datos actuales:**")
    datos_mostrados = False
    for categoria, tecnologias in t1.items():
        if tecnologias:  # Solo muestra categorías con datos
            print(f"\n🔹 {categoria}:")
            for tecnologia, cantidad in tecnologias.items():
                print(f"   - {tecnologia.capitalize()}: {cantidad}")
            datos_mostrados = True

    if not datos_mostrados:
        print("🔹 No hay datos registrados.")

def eliminar_tecnologia():
    """Permite eliminar una tecnología de una categoría específica."""
    if all(not tecnologias for tecnologias in t1.values()):
        print("❌ No hay datos para eliminar.")
        return

    print("\n📂 **Categorías disponibles:**")
    categorias_disponibles = [cat for cat in t1.keys() if t1[cat]]  # Filtra solo las que tienen datos
    for i, cat in enumerate(categorias_disponibles, 1):
        print(f"{i}. {cat}")

    cat_index = obtener_entero("\nElige el número de la categoría: ") - 1
    if 0 <= cat_index < len(categorias_disponibles):
        categoria = categorias_disponibles[cat_index]
        tecnologias = t1[categoria]

        print(f"\n📜 Tecnologías en {categoria}:")
        tecnologias_existentes = list(tecnologias.keys())
        for i, tech in enumerate(tecnologias_existentes, 1):
            print(f"{i}. {tech.capitalize()}")

        tech_index = obtener_entero("\nElige la tecnología a eliminar: ") - 1
        if 0 <= tech_index < len(tecnologias_existentes):
            tech_eliminar = tecnologias_existentes[tech_index]
            del t1[categoria][tech_eliminar]
            del tech_to_category[tech_eliminar]  # También eliminamos la referencia en tech_to_category
            print(f"✅ Tecnología '{tech_eliminar}' eliminada de {categoria}.")

        if not t1[categoria]:  # Si la categoría queda vacía, la mantiene vacía sin eliminarla
            print(f"ℹ️ La categoría '{categoria}' está ahora vacía.")
    else:
        print("❌ Opción inválida. Inténtalo de nuevo.")

while True:
    name = input("\nEscribe la tecnología: ").strip().lower()
    count = obtener_entero(f"¿Cuántas veces has visto {name}?: ")

    # Si la tecnología ya ha sido categorizada, la usamos directamente
    if name in tech_to_category:
        categoria = tech_to_category[name]
        print(f"📌 La tecnología '{name}' ya está en la categoría '{categoria}'.")
    else:
        categoria = seleccionar_categoria()
        tech_to_category[name] = categoria  # Guardamos la categoría para esta tecnología

    # Agregar al diccionario manteniendo el orden
    t1[categoria][name] = t1[categoria].get(name, 0) + count

    mostrar_datos()  # Muestra el estado actual

    # Preguntar si desea borrar un dato
    if input("\n¿Desea borrar algún dato? ('y' para sí, otra tecla para omitir): ").strip().lower() == "y":
        eliminar_tecnologia()
        mostrar_datos()

    # Opción para salir
    if input("\n¿Deseas salir? Presiona 'x', o cualquier tecla para continuar: ").strip().lower() == "x":
        break
