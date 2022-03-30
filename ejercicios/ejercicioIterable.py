dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
nom=int(input("Digite un dia de la semana: "))
while nom <= 0 or nom > 7:
  nom=int(input("ERROR: Porfavor Digite un dia de la semana VALIDO: "))
print(dias[nom-1])