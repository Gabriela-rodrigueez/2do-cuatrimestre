# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

nota_mayor =0
nota_menor =0

for i in range(10):
    nota=float(input(f"Debe ingresar sus 10 notas, ({i+1}) :"))
    
    if nota >=7:
        nota_mayor +=1
    else:
        nota_menor +=1
        
print(f"Notas mayores o iguales a 7: {nota_mayor} ")
print(f"Notas menor a 7: {nota_menor} ")