import random
import numpy
a0 = 1
a1 = 1
a2 = 3
a3 = 2

X1=[]
X2=[]
X3=[]
Xn1=[]
Xn2=[]
Xn3=[]
s=[]
f=[]

for i in range(8):
    X1.append(random.randrange(1,21,1))

for i in range(8):
    X2.append(random.randrange(1,21,1))

for i in range(8):
    X3.append(random.randrange(1,21,1))

Y = [a0 + a1*X1[i] + a2*X2[i] + a3*X3[i] for i in range(8)]
X01 = (max(X1)+min(X1))/2
X02 = (max(X2)+min(X2))/2
X03 = (max(X3)+min(X3))/2
dX1 = X01-min(X1)
dX2 = X02-min(X2)
dX3 = X03-min(X3)

for i in range(8):
    Xn1.append((X1[i] - X01)/dX1)
for i in range(8):
    Xn2.append((X2[i] - X02)/dX2)
for i in range(8):
    Xn3.append((X3[i] - X03)/dX3)

Ym=numpy.mean(Y)

for i in range(8):
    f.append((Y[i]-Ym))
for i in range(8):
    if f[i] > 0:
       s.append(f[i])
res = min(s)
print("a0=%s a1=%s a2=%s a3=%s"%(a0, a1, a2, a3))
print("X1: %s"%X1)
print("X2: %s"%X2)
print("X3: %s"%X3)
print("Y: %s"%Y)
print("x0: %s %s %s"%(X01, X02, X03))
print("dx: %s %s %s"%(dX1, dX2, dX3))
print("Xн1: %s"%Xn1)
print("Xн2: %s"%Xn2)
print("Xн3: %s"%Xn3)
print("Ym: %s"%Ym)
print("(Y-Ym): %s"%f)
print("min(Y-Ym): %s"%res)
