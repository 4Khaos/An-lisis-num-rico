import math
import sys
#----------------1-a---------------------
c=[2, 0, -3, 3, -4]
x=-2
cont=0
h=math.sqrt(sys.float_info.epsilon)

def horner ( a, x ):
    global cont
    res = a[0]
    for i in range ( 1, len(a)):
        res = x*res + a[i]
        cont = cont + 2 #Una suma y una multiplicacion

    return res
def derivada(c,x):
    global cont
    a = []
    a.extend(range(1,len(c)))
    co=len(c)-1
    for i in range(0,len(c)-1):
        a[i]=c[i]*co
        co= co -1
        cont=cont+1
    return a

def derivate (c,x):
    global cont
    cont = cont + 2
    return (horner(c, x + h) - horner(c, x)) / h


print ("Resultado función original: ", horner(c,x))
print("Operaciones basicas empleadas en función original: ", cont)
cont = 0
print("Derivada aproximada con epsilon: ",derivate(c,x))
print("Operaciones basicas empleadas en derivada aproximada: ", cont)
b = derivada( c , x )
cont = 0
print ("Derivada exacta: ",horner(b,x))
print ("Operaciones basicas empleadas en la derivada: " ,cont)
cont=0
horner(b,x)
print ("Operaciones basicas empleadas en Derivada exacta: ",cont)
