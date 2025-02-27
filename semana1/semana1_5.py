from primos import es_primo

numer1=int(input("Ingrese numero inicio: "))
numer2=int(input("Ingrese numero fin: "))

for num in range(numer1, numer2):
    if es_primo(num):
        print(num, end=" ")
