# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana
ventas = [[10, 5, 20, 7], [12, 8, 22, 9], [15, 6, 25, 10], [20, 9, 30, 11], [18, 7, 28, 12], [14, 10, 27, 8], [11, 12, 26, 6]]
dias_str = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
prodcuctos_str = ['Tv','Smartphone','Notebooks','Monitor']
acumladores_ventas_productos = [0] * len(ventas[0]) 
mayor_venta = -1
unidades_mas_vendidas = -1
print(f"\n{'Dia':<10} | {'ventas'}")
print(f"{'-'*20}")
for dia, productos in enumerate(ventas):    
    acumulador_ventas = 0        
    for producto, cantidad in enumerate(productos):
        # print(f"{dias_str[dia]} - {prodcuctos_str[producto]} - {cantidad}")
        acumulador_ventas += cantidad
        acumladores_ventas_productos[producto] += cantidad
    print(f"{dias_str[dia]:<10} | {acumulador_ventas:>5}")        
    if acumulador_ventas > mayor_venta:
        mayor_venta = acumulador_ventas
        dia_mas_ventas = dias_str[dia]
print(f"\nEl dia {dia_mas_ventas} con {mayor_venta} ventas, fue el dia con mas ventas")

print(f"\n{'Producto':<10} | {'ventas'}")
print(f"{'-'*20}")
for item, cantidades in enumerate(acumladores_ventas_productos):
    if cantidades > unidades_mas_vendidas:
        unidades_mas_vendidas = cantidades
        producto_mas_Vendido = item
    print(f"{prodcuctos_str[item]:<10} | {cantidades:>5}")
print(f"\nEl producto mas vendido fue {prodcuctos_str[producto_mas_Vendido]} con {unidades_mas_vendidas} unidades vendidas\n")
