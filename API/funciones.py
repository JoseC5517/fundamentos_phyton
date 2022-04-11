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
  print("\n\nhabilidades:\n")
  print ("{:<5} {:<40} ".format('ID','Nombre'))
  print("-"*20)
  for habilidad in range(len(datos['abilities'])):
    id = datos['abilities'][habilidad]['ability']['url'].split('/')[6]
    nombre = datos['abilities'][habilidad]['ability']['name']
    print("{:<5} {:<40} ".format(id,nombre))
    
def tiposPoke(datos):
  print("\n\ntipos:\n")
  print ("{:<5} {:<40} ".format('ID','Nombre'))
  print("-"*20)
  for tipo in range(len(datos['types'])):
    id = datos['types'][tipo]['type']['url'].split('/')[6]
    nombre = datos['types'][tipo]['type']['name']
    print("{:<5} {:<40} ".format(id,nombre))
    
def verPokemonID(BASE_URL,id_digitado):
  url1 = BASE_URL + f"pokemon/{id_digitado}"
  respuesta11 = requests.get(url1)
  if respuesta11:
    datos=respuesta11.json()
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format('ID','Nombre','Altura','# de Habilidad', '# de Movimientos\n'))
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format(id_digitado,datos['name'],int(datos['weight'])/10,datos['height']/10, len(datos['abilities'])))
  return datos

def verPokemonnom(BASE_URL,nom_digitado):
  url1 = BASE_URL + f"pokemon/{nom_digitado}"
  respuesta11 = requests.get(url1)
  if respuesta11:
    datos=respuesta11.json()
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format('ID','Nombre','Altura','# de Habilidad', '# de Movimientos\n'))
  print ("{:<5} {:<15} {:<10} {:<20} {:<10}".format(datos['id'],datos['name'],int(datos['weight'])/10,datos['height']/10, len(datos['abilities'])))
  return datos
  
def buscarPokemonPorId(primero,ultimo,REGEX_NUMBERS):
  id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
  resultado = re.search(REGEX_NUMBERS, id_digitado)
  
  while(not re.search(REGEX_NUMBERS, id_digitado)) or (int(id_digitado) < primero or int(id_digitado) > ultimo):
    id_digitado = input(f"Digite un id [{primero}-{ultimo}]:")
  return id_digitado
  
def buscarPokemonPorNombre(REGEX_NOMBRES,url):
  nom_digitado = input(f"Digite un nombre: ")
  resultado = re.search(REGEX_NOMBRES, nom_digitado)
  respuesta11 = requests.get(url)
  l = []
  if respuesta11:
    datos=respuesta11.json()
    for x in range(len(datos['results'])):
      l.append(datos['results'][x]['name'])
  while(not re.search(REGEX_NOMBRES, nom_digitado)):
    nom_digitado = input(f"Digite un nombre: ") 
  while not nom_digitado in l:
    nom_digitado = input(f"Digite un nombre valido: ") 

  return nom_digitado
def salir():
  print("bye")