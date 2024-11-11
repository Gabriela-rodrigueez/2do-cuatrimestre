# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

aptas=0

n=int(input("ingrese la cantidad de piezas a procesar: "))

for i in range(n):
    longitud =float(input(f"ingrese la longitud de la pieza {i+1}: "))
    # {i+1} "ingre la longitud de la pieza 1...2....3....4" se va actualizando el num de piezas 
    
    if 1.20 <= longitud <=1.30:
        aptas +=1

print(f"la cantidad de piezas aptas son: {aptas} ")
