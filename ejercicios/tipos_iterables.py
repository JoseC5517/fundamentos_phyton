dias = []
cant= int(input("Digite la cantidad de dias a ingresar: "))
for x in range(1,cant+1):
  digitar = input(f"Digite el dia {x}: ")
  dias.append(digitar)
print("\nDias ingresados:\n")
for dia in dias:
  print(dia)
