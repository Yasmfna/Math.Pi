print ("FICHIER DE CALCUL DE FONCTION MATHEMATIQUE")

#fonction de Fibonacci 
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    
    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
#on entre la valeur ici
n = int(input("Entrer un nombre ,afin de calculer son fibonnacci :"))
 
print(Fibonacci(n))
 
