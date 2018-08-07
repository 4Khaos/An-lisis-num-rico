import math
import sys
import matplotlib.pyplot as plt
e=math.sqrt(sys.float_info.epsilon)
def ecuacion(x):
    return(5*x)-pow(e,x)+1-2
i=-0.5
A=[]
C=[]
while(i<0.5):
    A.append(ecuacion(i))
    C.append(i)
    i=i+0.0001
    if(ecuacion(i)>=0.000 and ecuacion(i)<=0.001):
        print ("las raices son: ",round(i,4))
plt.plot(C,A, color='blue')
plt.show()