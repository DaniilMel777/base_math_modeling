import numpy as np
def my_func(a,b,n):
  x=np.linspace(a,b,n)
  y=x**2
  return y
print(my_func(1,100,2))