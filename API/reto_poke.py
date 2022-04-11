import requests
import re
from funciones import *
#constantes

BASE_URL = "https://pokeapi.co/api/v2/"
REGEX_NUMBERS = "^[0-9]{1,3}$"
REGEX_NOMBRES = "^[a-zA-Z]{1,10}$"

limite=input("Digite la cantidad a mostrar de pokemones: ")

while not re.search(REGEX_NUMBERS, limite):
  limite=input("Digite la cantidad a mostrar de pokemones: ")

x2 = 0
  
while x2 in range(899):
  limite = int(limite)
  url = BASE_URL+f"pokemon?limit={limite}&offset={x2}"
  
  verListado(url)
  listadoPokemones= obtenerDatos(url)
  primeroUltimo = obtenerPrimerUltimo(listadoPokemones['results'])
  
  print(primeroUltimo)
  
  primero = primeroUltimo[0]
  ultimo = primeroUltimo[1]
  
  
  conf = input("Desea buscar el pokemon por nombre y/n: ")
  
  while True:
      patron = "^[yn]{1}$"
      resultado22 = re.search(patron, conf)
      if resultado22:
          break
      conf = input("Desea buscar el pokemon por nombre y/n: ")
  
  if conf == "y":
    nom_digitado = buscarPokemonPorNombre(REGEX_NOMBRES,url)
    datos1 = verPokemonnom(BASE_URL,nom_digitado) 
    
  else:
    id_digitado = buscarPokemonPorId(primero,ultimo,REGEX_NUMBERS)
    datos1 = verPokemonID(BASE_URL,id_digitado)
  habilidadesPoke(datos1)
  tiposPoke(datos1)

  pag = input("Desea cambiar a la seguiente pagina a/s: ")
  while True:
    patron2 = "^[as]{1}$"
    resultado2 = re.search(patron2, pag)
    if resultado2:
        break
    pag = input("Desea cambiar a la seguiente pagina a/s: ")
    
  if pag == "s":
    x2 = x2 + limite
  else:
    x2 = x2 - limite




    

