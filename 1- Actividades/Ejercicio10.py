# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
	# if valor%2==0:
 
pares=0
impares=0

n=int(input("ingrese la cantidad de números: "))

for i in range(n):
	num = int(input(f"ingresar numeros {i+1} :"))
	
	if num % 2 ==0:
		pares +=1
	else:
		impares +=1

print(f"los valores pares son: {pares} ")
print(f"los valores impares son: {impares} ")
