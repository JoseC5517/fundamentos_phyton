import requests
import re
#constantes

BASE_URL = "https://pokeapi.co/api/v2/"
REGEX_NUMBERS = "^[0-9]{1,3}$"

limite=input("Digite la cantidad a mostrar de pokemones: ")

while not re.search(REGEX_NUMBERS, limite):
  limite=input("Digite la cantidad a mostrar de pokemones: ")

url = BASE_URL+f"pokemon?limit={limite}&offset=0"
respuesta = requests.get(url)

if respuesta:
  datos = respuesta.json()

  primero = None 
  ultimo = None 
  
  for pokemon in datos['results']:
    id_pokemon = pokemon['url'].split('/')[6]
    nombre= pokemon['name']
    if primero == None:
      primero = int(id_pokemon)
      
    print(id_pokemon, nombre)

  ultimo = int(id_pokemon)

  id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
  resultado = re.search(REGEX_NUMBERS, id_digitado)

  while not resultado:
    id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
    resultado = re.search(REGEX_NUMBERS, id_digitado)

  id_digitado = int(id_digitado)
  while id_digitado < primero or id_digitado > ultimo:
    id_digitado = int(input(f"Digite un id valido [{primero}-{ultimo}]:"))
else: 
  print(f"Ocurrio un error ({respuesta.status_code}) al obtener los datos")