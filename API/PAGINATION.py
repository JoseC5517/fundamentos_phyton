import requests

url = f"https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"
respuesta = requests.get(url)
datos=respuesta.json()
nombres=[]

for x in range(len(datos['results'])):
  nombres.append(datos['results'][x]['name'])
  
for i,x in enumerate(nombres,1):
  print(f"{i}. {x}")

pag = input("Desea ver la siguiente pagina (y/n): ").lower().replace(" ","")
if pag == "y":
  url = f"https://pokeapi.co/api/v2/pokemon?limit=20&offset=21"
  respuesta = requests.get(url)
  datos=respuesta.json()
  nombres=[]
  for x in range(len(datos['results'])):
    nombres.append(datos['results'][x]['name'])
  
  for i,x in enumerate(nombres,21):
    print(f"{i}. {x}")
