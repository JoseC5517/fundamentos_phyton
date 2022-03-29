#Aritmetrica
print("Aritmetrica\n")
suma = 5 + 15
print(suma, type(suma))

resta = 5 - 15
print(resta, type(resta))

multiplicar = 5 * 15
print(multiplicar, type(multiplicar))

dividir = 5 / 15
print(dividir, type(dividir))

potencia = 5 ** 15
print(potencia, type(potencia))

divEntera = 5 // 15
print(divEntera, type(divEntera))


#Relacionales
print("\n\nRelacionales\n")
a = 5 > 15
print(a, type(a))

a = 5 < 15
print(a, type(a))

a = 5 == 15
print(a, type(a))

a = 5 >= 15
print(a, type(a))

a = 5 <= 15
print(a, type(a))

a = 5 != 15
print(a, type(a))


#Logicos
print("\n\nLogicos\n")
a = 5 == 5 and 15 == 10
print(a, type(a))

a = 5 == 5 or 15 == 10
print(a, type(a))

a = not(5 == 5 and 15 == 10)
print(a, type(a))

a = 5 == 5 and 15 == 10
print(a, type(a))

#Pertenencia
print("\n\nPertenecia\n")
a = 5 in range(1,15)
print(a, type(a))

a = 5 not in range(1,15)
print(a, type(a))

#Identidad
print("\n\nIdentidad\n")

a = 5
b = 5

print(a is b,type(a==b))
print(a is not b,type(a==b))

#PROGRAMA QUE ME DIGA SI UNA PERSONA ES MAYOR O MENOR DE EDAD

nombre= input("\n\nComo te llamas?\n")
edad=int(input("\nCuantos anos tienes?\n"))
if edad >=18:
  print("Eres mayor de edad.")
else:
  print("Eres menor de edad. ")

num=int(input("\nDigite un numero: "))
if num>0:
  print("El numero digitado es positivo")
elif edad == 0:
  print("Es  igual 0")
else:
  print("El numero digitado es negativo")