class Numeros_romanos():
    def funcion(number):
        num= [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        simbolo=["M","CM","D","XD","L","XL","X","IX","V","IV","I"]

    
        while (True):
            ing_num= int(input("ingrese un numero entero: "))

            if ing_num==0:
                break

            print str(ing_num) + ":"

            i=0
        
        while (ing_num>0):
            if (ing_num >= num[i]):
                print str(num[i])
                ing_num = ing_num - num[i]
            
            else:
                i=i+1

    funcion()