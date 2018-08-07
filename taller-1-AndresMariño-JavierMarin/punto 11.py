import math


def evalFunc(f, x):
    return eval(f)


fx = '(x-5)*(x-4)*(x+7)'
p0 = 1.0
p1 = 3.0
p2 = -10.0
f0 = evalFunc(fx, p0)
f1 = evalFunc(fx, p1)
f2 = evalFunc(fx, p2)
tolerancia = 0.000001
print("f(x) = ", fx)
print("Las estimaciones iniciales son:")
print("f(", p0, ") = ", f0)
print("f(", p1, ") = ", f1)
print("f(", p2, ") = ", f2)
count = 0
print('{:2}: estimado a la raíz es f({:18.14f}) = {:18.14f}'.format(count, p0, f0))
fp3 = 1e9

while count < 30 and abs(fp3) >= tolerancia:
    f0 = evalFunc(fx, p0)
    f1 = evalFunc(fx, p1)
    f2 = evalFunc(fx, p2)

    o = f1 - f2
    n = f0 - f2
    s = p1 - p2
    r = p0 - p2
    denom = r * s * (p0 - p1)
    a = (s * n - r * o) / denom
    b = ((r ** 2) * o - (s ** 2) * n) / denom
    c = f2
    count += 1

    # RAICES
    x1 = (-2 * c) / (b + (b ** 2 - 4 * a * c) ** .5)
    x2 = (-2 * c) / (b - (b ** 2 - 4 * a * c) ** .5)

    if b > 0:
        p3 = p2 + x1
    else:
        p3 = p2 + x2

    fp3 = evalFunc(fx, p3)
    print('{:2}: estimado a la raíz es f({:18.14f}) = {:18.14f}'.format(count, p3, fp3))
    p0, p1, p2 = p1, p2, p3