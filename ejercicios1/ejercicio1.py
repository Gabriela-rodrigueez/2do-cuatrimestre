lista=[]
pares=[]
impares=[]
def funcion():  
    for i in range(8):
        num=int(input("ingrese 8 numeros: "))
        lista.append(num)
        if num %2==0:
            pares.append(num)
            print(f"la lista de numeros pares es: {pares}")
        else:
            num%2!=0
            impares.append(num)
            print(f"la lista de numeros impares es: {impares}")
funcion()