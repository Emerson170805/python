print("Imprime numeros pares: ")
numero1 = int(input("Del numero: "))
numero2 = int(input("Hasta el: "))

for i in range (numero1,numero2):
    if i % 2 == 0 :
        print(f"El numero: {i} par")
    else:
        print(f"El numero: {i} Es impar")