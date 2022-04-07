import requests
import re
from funciones import *
#constantes

BASE_URL = "https://pokeapi.co/api/v2/"
REGEX_NUMBERS = "^[0-9]{1,3}$"

limite=input("Digite la cantidad a mostrar de pokemones: ")

while not re.search(REGEX_NUMBERS, limite):
  limite=input("Digite la cantidad a mostrar de pokemones: ")

url = BASE_URL+f"pokemon?limit={limite}&offset=0"

verListado(url)

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
  while(not re.search(REGEX_NUMBERS, id_digitado)) or (int(id_digitado) < primero or int(id_digitado) > ultimo):
    id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
  
  url1 = BASE_URL + f"pokemon/{id_digitado}"
  respuesta11 = requests.get(url1)
  if respuesta11:
    datos=respuesta11.json()
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format('ID','Nombre','Altura','# de Habilidad', '# de Movimientos\n'))
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format(id_digitado,datos['name'],int(datos['weight'])/10,datos['height']/10, len(datos['abilities'])))

  habilidades = []
  tipos = []
  id1 = None
  print("\n\nhabilidades:\n")
  print ("{:<5} {:<40} ".format('ID','Nombre'))
  print("-"*20)
  for habilidad in range(len(datos['abilities'])):
    id = datos['abilities'][habilidad]['ability']['url'].split('/')[6]
    nombre = datos['abilities'][habilidad]['ability']['name']
    print(f"{id}    {nombre}")

else: 
  print(f"Ocurrio un error ({respuesta.status_code}) al obtener los datos")