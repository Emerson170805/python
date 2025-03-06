letra=input('Que letra desea buscar: ')
contador=input("Ingrese la palabra: ").lower().count(str(letra))
if contador>0:
    print(f"La palabra se repite {contador} veces")
else:
    print(f"La palabra {letra} no existe")