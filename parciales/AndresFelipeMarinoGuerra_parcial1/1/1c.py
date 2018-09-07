c = 0
n = 6
total = 0
for i in range (1,n*n + 1):
     sqr = i*i
     total = total + sqr
     c = c + 2
print ("total: ", total)

print ("numero de operaciones: ", c)

print ("La complejidad O del algoritmo es O(2*n^2) aproximado a O(n^2)")
