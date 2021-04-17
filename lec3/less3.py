import numpy as np
x0=0
y0=0
g=9.8
vx=1
vy=2
t=np.arange(0, 10, 0.1)
x=x0+vx*t
y=y0+vx*t-(g*t**2)/2
print(y)