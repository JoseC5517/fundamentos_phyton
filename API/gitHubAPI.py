import re
import requests
import webbrowser
while 1==1:
  usuario = input("Digite el usuario: ").replace(" ","")
  if usuario != "":
    break
while 1 == 1:
  patron = "^[a-zA-Z0-9]{3,15}$"
  resultado = re.search(patron, usuario)
  if resultado:
    print(usuario)
    break
  else:
    usuario = input("Digite el usuario: ").replace(" ","")
    
url = f"https://api.github.com/users/{usuario}"
respuesta = requests.get(url)
if respuesta:
  datos = respuesta.json()
  print(f"\n*USUARIO ENCONTRADO*\n\nUSUARIO: {datos['login']}\nNOMBRE: {datos['name']}\nFOLLOWERS: {datos['followers']}\nFOLLOWINGS: {datos['following']}\nPUBLIC RESPO: {datos['public_repos']}")
else:
  print("Usuario no encontrado!!")
  crear=input("Deseas crear uno (y/n): ").lower().replace(" ","")
  if crear == "y":
    webbrowser.open("https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home", new=2, autoraise=True)
  else:
    print("Hasta luego. #keepcoding")