# Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.

num=int(input("ingrese un número positivo: "))

if num >1:
    
    for i in range(1, num+1):
        print(i)
    else:
        print("el número ingresafo debe ser positivo")