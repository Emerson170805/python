numeros=[]

cantidad=int(input("Ingrese cuantos numeros quieres agregar: "))

for i in range (1,cantidad+1):
    numeros.append(int(input(f"Ingrese {i} numero: ")))
    
print(sorted(numeros))