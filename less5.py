a=input("Введите номер фигуры чтоб узнать её площадь\nтреугольник(1)\nкруг(2)\nпрямоугольник(3)\nромб(4)\n")
if a=="1":
  h=input('Введите длину высоты:')
  b=input('Введите длину стороны к которой проведена высота:')
  s1=(1/2)*float(b)*float(h)
  print("Площадь треуголника:", s1, "см")
elif a=="2":
  r=input("Введите длину радиуса:")
  p=3.14
  s2=p*(float(r)**2)
  print("Площадь круга:", s2, "см")
elif a=="3":
  g=input("Введите длину 1стороны:")
  j=input("Введите длину 2стороны:")
  s3=float(g)*float(j)
  print("Площадь прямоугольника:", s3, "см")
elif a=="4":
  k=input("Введите номер способа\nЧерез диагонали(1)\nЧерез высоту и сторону(2)\n")
  if k=="1":
    d1=input("Введите длину 1диагонали:")
    d2=input("Введите длину 2диагонали:")
    s4=(1/2)*float(d1)*float(d2)
    print("Площадь ромба:", s4, "см")
  elif k=="2":
    h1=input("Введите длину высоты:")
    a5=input("Введите длину стороны к которой проведена высота")
    s5=float(a5)*float(h1)
    print("Площадь ромба:", s5, "см")
