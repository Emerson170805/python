def es_primo(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

num=int(input("Ingrese cantidad:"))


for numero in range(num):
    if es_primo(numero):
        print(f"{numero} es un número primo.")
