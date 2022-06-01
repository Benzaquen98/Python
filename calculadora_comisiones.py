nombre = input("Por favor ingresa tu nombre: ")
venta = float(input("Ingresa por favor el monto vendido: "))
comisión = ((venta*13)/100)
print(f"hola {nombre}, vendiste {venta}, por lo cual tu comisión es de: {round(comisión, 2)} y el monto total es de: {round(venta+comisión,2)}")
