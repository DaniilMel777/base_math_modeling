import numpy as np
def my_func(a, n):
  n=int(n)
  if a==0:
    print("error")
  else:
    s=1
    if n>0:
      for i in range(0, abs(n)):
        s=s*a
    elif n==0:
      s=1
    elif n<0:
      for i in range(0, abs(n)):
        s=s/a
  return s
print(my_func(5,-4))
  