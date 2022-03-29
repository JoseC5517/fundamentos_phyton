print("AUTOR: Jose C. Encarnacion")
nom=input("Digite Su Nombre: ")
while 1 == 1:
  edad=int(input("Digite Su Edad: "))
  if edad in range(1,121):
    break
  else:
    print("ERROR: Su edad debe de estar en el rango (1-120) anos")
print("""\n
      1. SUMA
      2. RESTA
      3. MULTIPLICACION
      4. DIVICION\n""")
while 1 == 1:
  op=int(input("Cual operacion desea realizar: "))
  if op in range(1,5):
    break 
  else:
    continue
num=float(input("Porfavor, Digite un numero: "))
num2=float(input("Digite otro numero: "))
if op == 1:
  print(f"La suma de {num} + {num2} = {num+num2}")
elif op == 2:
  print(f"La resta de {num} - {num2} = {num-num2}")
elif op == 3:
  print(f"La multiplicacion de {num} * {num2} = {num*num2}")
else:
  if num2 != 0:
    print(f"La divicion de {num} / {num2} = {num/num2}")
  else:
    print(f"ERROR: NO SE PUEDE DIVIDIR{num} entre CERO.")