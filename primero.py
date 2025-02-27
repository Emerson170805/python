import numpy as np

columna1 = []  # Lista para cantidades
columna2 = []  # Lista para precios
cantidad = int(input("¿Cuántos productos va a llevar? "))
for i in range(cantidad):
    product = int(input(f"Ingrese cantidad del producto {i+1}: "))
    price = int(input(f"Ingrese precio del producto {i+1}: "))
    columna1.append(product)
    columna2.append(price)
productos = np.array(columna1)
precios = np.array(columna2)
precio_unitario = precios * productos
print("Los precios unitarios son:", precio_unitario)
print("La suma total es:", np.sum(precio_unitario))
print("Cantidad de productos por tipo:", columna1)
print("Cantidad total de productos:", np.sum(columna1))
print("Precios ingresados:", columna2)

