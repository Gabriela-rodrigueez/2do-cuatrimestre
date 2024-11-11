def funcion():
    num1=int(input("ingrese el primer num: "))
    num2=int(input("ingrese el segundo num: "))
    
    if num1>num2:
       print(1)
        
    elif num2>num1:
        print(-1)
    else:
        num1=num2
        print (0)
funcion()