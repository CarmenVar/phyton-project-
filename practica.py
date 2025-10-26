nombres_clientes = []
while True:
    nombre = input("Ingresá el nombre del cliente (o escribí 'fin' para terminar : ").strip()
    if not nombre:
        print("El nombre no puede estar vacío. Por favor, ingresá un nombre válido.")
        continue
    if nombre.lower() == "fin":
        print("✅ Finalizando carga de nombres...")
        break
    nombres_clientes.append(nombre)
    print(f"✅ Nombre registrado: {nombre}")
    
    nombres_clientes.sort()
    print("\n📋 Lista de clientes ordenada alfabéticamente:")
for nombre in nombres_clientes:
    print(f"🔹 {nombre}")
        
    