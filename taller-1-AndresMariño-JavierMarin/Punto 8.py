import math
import matplotlib.pyplot as plt

def r1 (t):
    return 2.0 + math.cos(3.0*t)

def r2(t):
    return 2.0 - math.exp(t)


A = []
B = []
C = []
res = []
i = -10.0
while (i < 4.0):
    A.append (r1(i))
    B.append (r2(i))
    C.append (i)
    i = i+0.001
    if ( abs((r1(i) - r2(i))) < 0.001 ):
        res.append(r1(i))

print("los puntos de interseccion son: ", res)
plt.plot(C,A, color='red')
plt.plot(C,B, color='blue')
plt.show()