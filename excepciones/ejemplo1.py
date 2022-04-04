edad = int(input("digite una edad:"))
if edad < 18:
  raise Exception("No puede ser menor.")
print("El leo...")

try:
  num1 = int(input("Digita numero 1: ")) 
  num2 = int(input("Digita numero 1: ")) 
  resultado = num1 / num2
except TypeError:
  print("Error de tipeo")
except ZeroDivisionError:
  print("No se puede dividir entre 0")
  