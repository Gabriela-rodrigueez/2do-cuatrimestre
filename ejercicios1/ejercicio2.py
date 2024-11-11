def factorial():
    num=int(input("ingrese un numero ENTERO POSITIVO: "))
    factorial=1
    if num<0:
        print("el numero es negativo")
    elif num ==0:
        return 1
    else:
        for i in range(1,num+1):
            factorial= factorial*i
        print(f"el factorial del {num} es: {factorial}")
            
factorial()