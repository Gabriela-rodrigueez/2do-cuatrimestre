# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

personas=0
sueldo=0
sueldo1=0
sueldo2=0
sueldo_total=0
gastos=0

n=int(input("ingrese el número de empleados: "))

for i in range(n):
    sueldo= float(input("ingresar sueldo: "))
    
    if sueldo >=100 and sueldo <=300:
        sueldo1 +=1
        
    elif sueldo >300:
        sueldo2 +=1
        
    gastos += sueldo
    
print(f"los empleados que cobran entre $100 y $300 son: {sueldo1} ")
print(f"los empleados que cobran más de $300 son: {sueldo2} ")
print(f"los gastos de la empresa son: {gastos} ")