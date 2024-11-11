def iva():
    cantidad=float(input("ingrese la cantidad sin iva: "))
    porcentaje_iva=float(input("ingrese el % de iva por aplicar: "))
    iva= cantidad* porcentaje_iva
    aplicar_iva=0.21
    for i in range (1):
        if iva:
            total= cantidad *iva
            print(total)
        else:
            porcentaje_iva==0
            iva2= cantidad * aplicar_iva
            total2= cantidad + iva2
            print(total2)


iva()