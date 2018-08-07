def volumen(n):
    return (768*n-112*pow(n,2)+4*pow(n,3))-1000
def funcion(a,b,e,d):
    x=a
    if(d>e):
        if(volumen(x)<0):
            return (funcion(x + d, b, e, d))
        else:
            x=x-d
            d=d/10
            x=x+d
            return (funcion(x,b,e,d))
    else:
        return (x)
a=int(input("ingrese el rango menor: "))
b=int(input("ingrese el rango mayor: "))
print(round(funcion(a,b,0.00001,(b-a)/10),5))