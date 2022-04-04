import requests
x1 = 0
x2 = int(input("Cuantos resutados quieres ver por pagina: "))
while x1 <= 898:
  url = f"https://pokeapi.co/api/v2/pokemon?limit={x2}&offset={x1}"
  respuesta = requests.get(url)
  datos=respuesta.json()
  nombres=[]
  for x in range(len(datos['results'])):
    nombres.append(datos['results'][x]['name'])
  
  for i,x in enumerate(nombres,1):
    print(f"{i+x1}. {x}")

  pag = input("Desea ver la siguiente pagina (y/n): ").lower().replace(" ","")
  
  if pag == "n":
    break
  else:
    x1 = x1 + x2