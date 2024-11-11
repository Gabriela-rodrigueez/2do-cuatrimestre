lista=[]
notas=int(input("ingrese la cantidad de notas: "))

for contador in range (notas):
    calificacion = float(input("ingrese cada nota: "))
    lista.append(calificacion)
    suma=sum (lista) 
    promedio= suma/notas
print(f"El promedio de sus notas es: {promedio}")
    
    
    