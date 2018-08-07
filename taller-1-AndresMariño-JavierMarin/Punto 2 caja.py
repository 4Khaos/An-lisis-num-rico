import math
def volumen(n):
    return 768*n-112*pow(n,2)+4*pow(n,3)
def biccecion(x,y,v):
    global e
    global n
    c=(y-x)/2+x
   # print(n-c,"  ",e)
    if(abs(n-c)>=e):
        if(volumen(c)==v):
            return (c)
        else:
            if(volumen(c)<v):
                return biccecion(c,y,v)
            else:
                if(volumen(c)>v):
                    return biccecion(x,c,v)
    else:
        return (c)
b=32
h=24
v=1000
a=int(input("ingrese el rango menor: "))
b=int(input("ingrese el rango mayor: "))
e=0.00001
n=a
while(n<=b):
    x=volumen(n)
    if(x>v):
        print("x es igual por formato de un while: ",n-e)
        break
    n=n+e
print("Con bissecion es:",round(biccecion(a,b,v),5))
