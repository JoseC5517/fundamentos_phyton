#Imprimir caracteres pares de un nombre digitado
nom=[]
nom1=input("Ingrese Su nombre: ")
nom.append(nom1)
for nombre in nom:
    print(nombre[1::2])
