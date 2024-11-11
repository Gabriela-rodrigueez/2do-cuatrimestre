# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

lista1=[]
lista2=[]

for i in range(15):
    lista1.append(float(input(f"ingrese valor {i+1} de la lista 1: ")))
    lista2.append(float(input(f"ingrese valor {i+1} de la lista 2: ")))
    
suma_lista1= sum(lista1)
suma_lista2= sum(lista2)

if suma_lista1>suma_lista2:
    print("Lista 1 Mayor")
    
elif suma_lista1<suma_lista2:
    print("Lista 2 Mayor")
    
else:
    print("Listas iguales")
    
    
    
    