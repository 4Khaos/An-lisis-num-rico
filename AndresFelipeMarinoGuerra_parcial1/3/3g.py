import time

def evalFunc(x1,x2,x3,x4,i,a):

    a1 = (a[i][0])*x1

    a2 = (a[i][1])*x2

    a3 = (a[i][2])*x3

    a4 = (a[i][3]) * x4

    return ( a1 + a2 + a3 + x4  )/ a[i][i]

a=[[4,-1,-1,-1],[-1,4,-1,-1],[-1,-1,-1,4],[-1,-1,-1,4]]

x1 = 0

x2 = 0

x3 = 0

w = 0.8

e=0.0000001

isM = True

while(isM):

    x=abs(((a[0][0]*x1)+(a[0][1]*x2)+(a[0][2]*x3))-a[0][3])

    print("formula 1 es: ",x, "x1: ", x1, "x2: ", x2, "x3: ", x3)

    x1 = evalFunc((1-w)*x1, -x2*w, -x3*w, a[0][3]*w,0,a)

    x2 = evalFunc(-x1*w, (1-w)*x2, -x3*w, a[1][3]*w,1,a)

    x3 = evalFunc(-x1*w, -x2*w, (1-w)*x3, a[2][3]*w,2,a)

    x4 = evalFunc(-x1*w, -x2*w, -x3*w, a[3][3]*w,3,a)



    time.sleep(0.2)

    if(x<=e):

        isM=False