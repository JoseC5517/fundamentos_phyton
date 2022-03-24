#convertidor de peso a dolar
print(
  """Bienvenido/a a este Convertidor 
        De Peso a Dolar""",end="\n\n"
)
nombre=input("Como te llamas: ")
cant=float(input("Ingrese una cantidad: "))
resultado=round(cant/55.15,2)
print("Cambio realizado con exito:\nUsuario: ",nombre,"\nIngresaste: ",cant," Pesos\nCambio a Dolar: $",resultado)
