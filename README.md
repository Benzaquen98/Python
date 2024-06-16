print("Bienvenido a la Ferreteria de Yigal, su ferretería de confianza")

productos = {
    "Jardinería": {"precio": 15000, "descuento": 10},
    "Metales": {"precio": 25000, "descuento": 15},
    "Pisos": {"precio": 14000, "descuento": 5},
    "Mascotas": {"precio": 25000, "descuento": 2}
}

def mostrar_productos():
    print("\nProductos disponibles:")
    for llave, (producto, datos) in enumerate(productos.items(), 1):
        print(f"{llave}. {producto} - Precio: {datos['precio']} - Descuento: {datos['descuento']}%")

def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad

def aplicar_descuento(precio_total, descuento):
    return (precio_total * descuento) / 100

def generar_factura(cliente, productos_comprados):
    total_factura = 0
    print("\nFactura")
    print(f"Cliente: {cliente}")
    for producto, detalles in productos_comprados.items():
        cantidad = detalles['cantidad']
        precio_unitario = detalles['precio_unitario']
        precio_total = detalles['precio_total']
        descuento_aplicado = detalles['descuento_aplicado']
        precio_con_descuento = detalles['precio_con_descuento']

        print(f"Producto: {producto}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio Unitario: {precio_unitario}")
        print(f"Total a pagar: {precio_total}")
        print(f"Descuento Aplicado (%): {descuento_aplicado}")
        print(f"Precio con Descuento: {precio_con_descuento}")
        
        total_factura += precio_con_descuento

    print(f"Total de la factura: {total_factura}")

mostrar_productos()

productos_comprados = {}

while True:
    try:
        opcion = int(input("\nIngrese el número del producto que desea comprar: "))
        if 1 <= opcion <= len(productos):
            producto_elegido = list(productos.keys())[opcion - 1]
            cantidad = int(input(f"Ingrese la cantidad de '{producto_elegido}' que desea comprar: "))
            precio_unitario = productos[producto_elegido]["precio"]
            descuento_producto = productos[producto_elegido]["descuento"]
            precio_total = calcular_total(precio_unitario, cantidad)
            descuento_aplicado = aplicar_descuento(precio_total, descuento_producto)
            precio_con_descuento = precio_total - descuento_aplicado

            if producto_elegido in productos_comprados:
                productos_comprados[producto_elegido]['cantidad'] += cantidad
                productos_comprados[producto_elegido]['precio_total'] += precio_total
                productos_comprados[producto_elegido]['descuento_aplicado'] += descuento_aplicado
                productos_comprados[producto_elegido]['precio_con_descuento'] += precio_con_descuento
            else:
                productos_comprados[producto_elegido] = {
                    'cantidad': cantidad,
                    'precio_unitario': precio_unitario,
                    'precio_total': precio_total,
                    'descuento_aplicado': descuento_aplicado,
                    'precio_con_descuento': precio_con_descuento
                }
                
            opcion_continuar = input("\nSi quiere comprar algo más digite 1, si no, presione 2 para generar la factura: ")
            if opcion_continuar != '1':
                break
        else:
            print("Opción no válida. Ingrese un número válido entre 1 y 4.")
    except ValueError:
        print("Debe ingresar un número.")

nombre_cliente = input("Por favor, ingrese su nombre para la factura: ")
generar_factura(nombre_cliente, productos_comprados)

print("\n¡Gracias por su compra!")
print("Vuelva pronto")
