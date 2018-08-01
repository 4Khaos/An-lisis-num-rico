def horner ( a, x ):
    res = a[0]
    operations = 0
    for i in range ( len(a)-2,-1 ,-1):
        res = res * x + a[i]
        operations = operations + 2 #Una suma y una multiplicacion

    print ("operaciones: ", operations )  
    return res
#Coeficientes de a0 a an
a = [3,4,5,6,2,3]
x = 8

print ( "resultado: ", horner ( a, x) )
