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
listadoPokemones= obtenerDatos(url)
primeroUltimo = obtenerPrimerUltimo(listadoPokemones['results'])

print(primeroUltimo)

primero = primeroUltimo[0]
ultimo = primeroUltimo[1]

id_digitado = buscarPokemonPorId(primero,ultimo,REGEX_NUMBERS)
datos = verPokemon(BASE_URL,id_digitado)
habilidadesPoke(datos)
tiposPoke(datos)


    

