from lec_4_my import *

tmp=mult_func(4)
print(tmp)
print(mult_func(10))
print(mult_func("godd"))
print_func("hello")
print_func(mult_func("50"))

x0=10
x=1
def move(t):
  x=x0*t
  return x0

print(move(3))
print(x)
a="good"

def my_func():
  a="bad"
  print(a)

my_func()
print(a)

a=500
print(id(a))
a=a+5
print(id(a))\

b=[500]
print(id(b))
b[0]=505
print(id(b))

#tuple кортеж
t=(1, 4, 9)
print(t)
print(t[0])

#dict
d={'al': 4, 4:'al', 'str':'hello'}
print(d['al'])
print(d[4])
print(d['str'])
d['str']='good'
print(d)

def my_func(a=1, b=0):
  x=3*a-b
  return x
print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))

a=[1, 2, 3, 4]
b=[*a, 5, 6, 7]
c=[a, 5, 6, 7]
print(c)
print(b)

def my_funk(*args):
  x=3*args[0]-args[1]
  return x

print(my_funk(3, 4))
print(my_funk(3, 4, 8))


def my_funh(**kwrgs):
  x=3*kwrgs['obj_l']-kwrgs['obj_2']
  return x
print(my_funh(obj_l=3, obj_2=4))
print(my_funh(obj_l=3, obj_2=4, obj_3=8))