from sys import argv
import sys
import numpy as np

name = argv[1]

#name = raw_input("Enter file:")
#if len(name) < 1 : name = "D:/Dropbox/CS/310_2016/LU-Decomposition/linearsolver_xinz_input_001.txt"

#b = []
#y = []

i=-1
for line in open(name, 'r').readlines():
    j = 0
    if i==-1:
        n = int(line)

        A = np.zeros(n*n).reshape(n, n)  #initalize martix A
        AP = np.zeros(n*(n+1)).reshape(n, n+1)
    elif i < n:
        rows=line.strip().split(" ")
        for e in rows:
            A[i, j]=float(e)
            AP[i, j]=float(e)
            j += 1
    elif i == n:
        rows=line.strip().split(" ")
        s = 0
        for e in rows:       
            #b.append(float(e))
            AP[s, i]=float(e)
            s += 1
    i += 1

if i != (n+1):
    print "inconsistent/indeterminant system."
    sys.exit()

x = [0 for i in range(n)]
#print x

for i in range(n): # i-th row
    pivotrow = i
    for j in range(i+1, n):
        if abs(AP[j, i]) > abs(AP[pivotrow, i]):
            pivotrow = j
    for k in range(i, n+1):
        swap = AP[i, k]
        AP[i, k] = AP[pivotrow, k]
        AP[pivotrow, k] = swap
    for j in range(i+1, n):
        if AP[i, i] == 0:
            print "inconsistent/indeterminant system"
            sys.exit()
        t = AP[j, i]/AP[i, i]
        for k in range(i, n+1):
            AP[j, k] = AP[j, k] - t*AP[i, k]
U = AP[:, :n]
#b = AP[:, n]

#print U
#print AP

#backsolving Ux=b
for i in reversed(range(n)):
    t = AP[i, n]
    for j in range(i+1, n):
        t = t - AP[i, j]*x[j]
    if AP[i, i] == 0:
        print "inconsistent/indeterminant system"
        sys.exit()
    else:
        x[i] = (t/AP[i, i])

print ' '.join([str(item) for item in x]) 
    
