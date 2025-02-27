numeros = [int(input(f"Ingrese el {i+1} numero: ")) for i in range(int(input("Ingrese cuantos numeros quieres agregar: ")))]
print(sorted(numeros))