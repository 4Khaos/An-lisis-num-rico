import math
n=int(input("ingrese un numero: "))
aux=n
cont=0
while(n>0):
    d=n%2
    n=int(n/2)
    cont = cont + 1
    print(n)
print("O(log(n)): ",math.log(aux,2))
