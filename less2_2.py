def my_func(*args):
  a=len(args)
  x=sum(args)/a
  return x
print(my_func(1, 2, 3, 4))
