import requests
import re

def obtenerPrimerUltimo(lista):
  primero = None 
  ultimo = None 
  for pokemon in lista:
    id_pokemon = pokemon['url'].split('/')[6]
    if primero == None:
      primero = int(id_pokemon)
      
  ultimo = int(id_pokemon)
  return (primero, ultimo)

def obtenerDatos(url):
  respuesta = requests.get(url)

  if respuesta:
    return respuesta.json()
  else:
    raise Exception("No hay datos")
  
def verListado(url):
  print("Listado de pokemones")
  
  respuesta = requests.get(url)
  if respuesta:
    datos = respuesta.json()


  
  for pokemon in datos['results']:
    id_pokemon = pokemon['url'].split('/')[6]
    nombre= pokemon['name']
  #   if primero == None:
  #     primero = int(id_pokemon)
      
    print(id_pokemon, nombre)

  # ultimo = int(id_pokemon)
def habilidadesPoke(datos):
  habilidades = []
  print("\n\nhabilidades:\n")
  print ("{:<5} {:<40} ".format('ID','Nombre'))
  print("-"*20)
  for habilidad in range(len(datos['abilities'])):
    id = datos['abilities'][habilidad]['ability']['url'].split('/')[6]
    nombre = datos['abilities'][habilidad]['ability']['name']
    print("{:<5} {:<40} ".format(id,nombre))
def verPokemon():
  print("ver pokemon")
  
def buscarPokemonPorId():
  print("Buscando ID")
  id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
  resultado = re.search(REGEX_NUMBERS, id_digitado)
  while(not re.search(REGEX_NUMBERS, id_digitado)) or (int(id_digitado) < primero or int(id_digitado) > ultimo):
    id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")

def buscarPokemonPorNombre():
  print("Buscando pokemon")
def salir():
  print("bye")