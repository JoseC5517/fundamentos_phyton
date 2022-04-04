import requests

url1 = f"https://pokeapi.co/api/v2/pokemon?limit=100&offset=200"
respuesta1 = requests.get(url1)
dt=respuesta1.json()

while 1 == 1:
  usuario = int(input(f"Digite el ID del pokemon entre 1 y {dt['count']}: "))
  if usuario in range(1,dt["count"]+1):
    break
    
url = f"https://pokeapi.co/api/v2/pokemon/{usuario}"
respuesta = requests.get(url)

if respuesta:
  datos=respuesta.json()
  habilidades = []
  tipos = []
  
  for habilidad in range(len(datos['abilities'])):
    habilidades.append(datos['abilities'][habilidad]['ability']['name'])
    
print(f"""
NOMBRE: {datos['name']}\n
PESO: {int(datos['weight'])/10}\n
ALTURA: {datos['height']}\n
CANTIDAD DE HABILIDADES: {len(datos['abilities'])}\n
HABILIDADES:""")  

for i,x in enumerate(habilidades,1):
  print(f"{i}. {x}")
  
print(f"""
CANTIDAD DE MOVIMIENTOS: {len(datos['moves'])}\n
TIPOS: """)

for tipo in range(len(datos['types'])):
  tipos.append(datos['types'][tipo]['type']['name'])
  
for i,x in enumerate(tipos,1):
  print(f"{i}. {x}")
  
#   idiomas=[]
#   habilidades=[]
#   for nombres in datos['names']:
#     idiomas.append(nombres['language']['name'])
#     habilidades.append(nombres['name'])
#   print("\nListado de idiomas.")
#   for i,idioma in enumerate(idiomas,1):
#     print(f"{i}. {idioma}")
#   print("\nListado de habilidades.")
#   for i,habilidad in enumerate(habilidades,1):
#     print(f"{i}. {habilidad}")
