import requests
usuario = int(input("Digite el ID del pokemon: "))
url = f"https://pokeapi.co/api/v2/pokemon/{usuario}"
respuesta = requests.get(url)
if respuesta:
  datos=respuesta.json()
  habilidades = []
  for habilidad in habilidades:
    habilidades.append(datos['abilities']['ability']['name'])
print(f"""NOMBRE: {datos['name']}
      PESO: {int(datos['weight'])/10}
      ALTURA: {datos['height']}
      CANTIDAD DE HABILIDADES: {len(datos['abilities'])}
      HABILIDADES:""")
for i,x in enumerate(habilidades,1):
  print(f"{i}. {idioma}")
  
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
