numero="536.78"
m = 4
x=numero.split('.')
def digitos(numero):
    x=numero.split('.')
    n=0
    for i in range(len(x)):
        n=n+len(x[i])
    return(n)
print("|E|< 1*10^",digitos(numero)-m)