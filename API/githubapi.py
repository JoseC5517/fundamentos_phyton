import os
import random
while 1 == 1:
  usu=input("\nDigite su usuario: ").replace(" ","").lower()
  url= os.path.exists(f"usuarios/{usu}.txt")
  if url == True:
    print(f"""*Usuario Encontrado*
          NOMBRE: {usu}
          FOLLOWERS: {random.randint(25, 1000)}
          FOLLOWING: {random.randint(25, 1000)}
          PUBLIC RESPO: {random.randint(1, 100)}""")
    conf=input("\nDesea continuar o finalizar el programa(y/n): ").replace(" ","").lower()
    if conf == "y":
      break
  else:
    print("Usuario No Encontrado.")
    registro=input("Desea Crear un Usuario? (y/n): ").replace(" ","").lower()
    if registro == "y":
      reg = input("Ingrese su nombre de usuario: ").replace(" ","").lower()
      file = open(f"usuarios/{reg}.txt","w")
      file.close()
    else:
      print("*PROGRAMA FINALIZADO*")


