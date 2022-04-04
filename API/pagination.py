import requests

url = f"https://pokeapi.co/api/v2/pokemon?limit=50&offset=0"
respuesta = requests.get(url)
datos=respuesta.json()
nombres=[]

for x in range(len(datos['results'])):
  nombres.append(datos['results'][x]['name'])
  
for i,x in enumerate(nombres,1):
  print(f"{i}. {x}")

