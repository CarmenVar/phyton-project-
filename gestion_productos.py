# Lista vacía para guardar los productos
productos = []

# Bucle principal del programa
while True:
    # Mostramos el menú
    print("\nSistema de Gestión de Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Elegí una opción: ")

    # Evaluamos la opción ingresada
    if opcion == "1":
        print("Elegiste: Agregar producto")
        while True:
            nombre = input("Nombre del producto: ").strip()
            if nombre:
                break
            else:
                print("El nombre no puede estar vacío.")
        while True:
            categoria = input("Categoría del producto: ").strip()
            if categoria:
                break
            else:
                print("La categoría no puede estar vacía.")
        while True:
            entrada_precio = input("Precio del producto (número entero): ")
            try:
                precio = int(entrada_precio)
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor que 0.")
            except ValueError:
                print("Ingresá un número válido.")
        productos.append([nombre, categoria, precio])
        print("✅ Producto agregado exitosamente.")

    elif opcion == "2":
        print("Elegiste: Mostrar productos")
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\n📋 Lista de productos:")
            for i, producto in enumerate(productos, start=1):
                nombre, categoria, precio = producto
                print(f"{i} {nombre} | {categoria} | ${precio}")
    elif opcion == "3":
        print("Elegiste: Buscar producto")
        termino = input("Ingresá el nombre o parte del nombre a buscar: ").strip().lower()

        resultados = []

        for i, producto in enumerate(productos, start=1):
            nombre, categoria, precio = producto
            if termino in nombre.lower():
                resultados.append((i, producto))

        if resultados:
            print("\n🔎 Resultados encontrados:")
            for i, producto in resultados:
                nombre, categoria, precio = producto
                print(f"{i}. {nombre} | {categoria} | ${precio}")
        else:
            print("No se encontraron productos con ese nombre.")

    elif opcion == "4":
        print("Elegiste: Eliminar producto")
    elif opcion == "5":
        print("Saliendo del programa... ¡Hasta luego!")
        break  # Esto termina el bucle while
    else:
        print("Opción no válida. Por favor, intentá de nuevo.")
