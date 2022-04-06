import requests
import re
x1 = 0
while 1==1:
  x2 = input("Cuantos resultados quieres ver por pagina: ").replace(" ","")
  if x2 != "":
    break
while 1 == 1:
  patron = "^[0-9]{1,3}$"
  resultado = re.search(patron, x2)
  if resultado:
    break
  else:
    x2 = input("Cuantos resultados quieres ver por pagina: ").replace(" ","")
while 1 == 1:
  url = f"https://pokeapi.co/api/v2/pokemon?limit={x2}&offset={x1}"
  respuesta = requests.get(url)
  datos=respuesta.json()
  nombres=[]
  for x12 in range(len(datos['results'])):
    nombres.append(datos['results'][x12]['name'])
  
  for i,x in enumerate(nombres,1):
    b = i + x1
    print(f"{b}. {x}")
    
  while 1==1:
    id = input(f"Digite el ID del pokemon: ").replace(" ","")
    if id != "":
      break
      
  while 1 == 1:
    patron = "^[0-9]{1,3}$"
    resultado22 = re.search(patron, id)
    if resultado22:
      if int(id) in range(x1+1,b+1):
        break
    id = input(f"Digite un ID valido: ").replace(" ","")



  url1 = f"https://pokeapi.co/api/v2/pokemon/{id}"
  respuesta1 = requests.get(url1)
  if respuesta1:
    datos=respuesta1.json()
    habilidades = []
    tipos = []
  
  for habilidad in range(len(datos['abilities'])):
    habilidades.append(datos['abilities'][habilidad]['ability']['name'])
  
  print(f"""
  NOMBRE: {datos['name']}\n
  PESO: {int(datos['weight'])/10} kg\n
  ALTURA: {datos['height']/10} m\n
  CANTIDAD DE HABILIDADES: {len(datos['abilities'])}\n
  HABILIDADES:""") 
  
  for ii,xd in enumerate(habilidades,1):
    print(f"{ii}. {xd}")
  
  print(f"""
  CANTIDAD DE MOVIMIENTOS: {len(datos['moves'])}\n
  TIPOS: """)
  
  for tipo in range(len(datos['types'])):
    tipos.append(datos['types'][tipo]['type']['name'])
  
  for i1,x6 in enumerate(tipos,1):
    print(f"{i1}. {x6}")

  while 1 == 1:
    pag = input("Digite (a/s) para cambiar de pagina: ").lower().replace(" ","")
    if pag == "a":
      x1 = x1 - int(x2)
      break
    elif pag == "s":
      x1 = x1 + int(x2)
      break
    else:
      continue
  if x1 not in range(1,899):
    break