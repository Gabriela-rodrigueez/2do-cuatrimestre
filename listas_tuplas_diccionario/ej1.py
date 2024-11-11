frutas = ["manzana","banana", " "]
print(frutas [0:1])
print (len(frutas))
print(frutas[-1])
frutas[2]="anana"
print(frutas)
frutas[1]="kiwi"
print(frutas)
frutas[2]="2"
print(frutas)
frutas.append(1)
print(frutas)
frutas.insert(1,"tomate")
print(frutas)
frutas.remove("kiwi")
print(frutas)
frutas.pop(1)
print(frutas)
del frutas[2]
print(frutas)

# las tuplas no se pueden modificar, ni eliminar, ni agregar nada; sonpara cosas en especifico(ej: sexo, tipo de sangre,etc)
lista1=("elemento1","elemento2","elemneto3")

# diccionarios se le colocan llaves y se separa por : , se puden modicicar, para eliminar algo se utiliza del. Y para acceder a un elemento del diccionario se utiliza get()
list={"nombre" :"juan", "apellido": "perez"}