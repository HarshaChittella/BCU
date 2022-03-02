a=9
b=8
c=12
d=33
e=5

Sum = a+b+c+d+e
print('Sum is ',Sum)

mean = Sum/5
print('mean is ',mean)

x = (a-mean)**2 + (b-mean)**2 + (c-mean)**2 + (d-mean)**2 + (e-mean)**2

Variance = x/5

deviation = Variance**(1/2.0)
print(deviation)