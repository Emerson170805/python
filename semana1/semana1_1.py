def primo(n):
    if n<2:
        return False
    if n in range (n, int(n**2)+1):
        if n%2==0:
            return True
    else:
        return True
    
numero=int(input("Ingrese numero: "))

if primo(numero):
    print("Numero primo: ",numero)
    
        