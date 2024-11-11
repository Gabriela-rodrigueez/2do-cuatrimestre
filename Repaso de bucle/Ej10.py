num=int(input("ingrese un num: "))
for i in range (2,num):
    if (num%i !=0):
        print("el num es primo")
        break
    else:
        print("el num no es primo")