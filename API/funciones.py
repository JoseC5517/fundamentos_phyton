import requests
def verListado(url):
  print("Listado de pokemones")
  
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
  
def verPokemon():
  print("ver pokemon")
def buscarPokemonPorId():
  print("Buscando ID")
def buscarPokemonPorNombre():
  print("Buscando pokemon")
def salir():
  print("bye")