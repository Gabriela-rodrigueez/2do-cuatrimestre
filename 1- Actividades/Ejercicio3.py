# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.

suma=0
contador=0

for i in range(10):
    num= float(input(f"Debe ingresar 10 números, ({i+1}) :"))
    suma +=num
    contador +=1
    promedio= suma/contador
    
print(f"la suma es: {suma} ")
print(f"el promedio es: {promedio} ")