import math as m
x=3
y=(m.sqrt(x**3))/((x**3)+(3/x))*(4*(x**7)-(x**5))+80*(m.sqrt(27*(x**4)+12*(x**3)-5*(x**2)+10))
a=(m.sqrt(x**3))/((x**3)+(3/x))
b=(4*(x**7)-(x**5))
c=80
d=(m.sqrt(27*(x**4)+12*(x**3)-5*(x**2)+10))
f=a*b+c*d
print(y)
print(f)