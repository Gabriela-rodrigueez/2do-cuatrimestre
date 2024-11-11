# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

suma_altura=0
personas=0

n=int(input("ingrese el número de personas: "))

for i in range(n):
    altura= float(input("ingrese la altura: "))
    suma_altura += altura
    personas +=1
    promedio= suma_altura/personas
    
print(f"la altura promedio es: {promedio} ")