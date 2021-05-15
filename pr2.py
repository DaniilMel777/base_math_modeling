g=9.8

def my_func(m,v,h):
  ek=m*(v**2)/2
  ep=m*g*h
  e=ek+ep
  return e
print(my_func(10, 5, 10))