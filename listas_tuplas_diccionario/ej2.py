lista=[20,50,"Curso","Python",3.14]
print(lista)
agregar1=input("ingrese el primer dato: ")
agregar2=input("ingrese el segundo dato: ")
lista[1]= agregar1
lista[2]= agregar2
print("el nuevo valor de la lista es: {}".format(lista))
print(lista)

for contador in lista:
    print(contador)
