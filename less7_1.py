import matplotlib.pyplot as plt
import numpy as np
x=[3, 4, 5]
y=[40, 10, 30]
plt.plot(x, y, color='g', label='luchte', marker='>', ms=5)
 

import matplotlib.pyplot as plt
import numpy as np
x=[3, 4, 10]
y=[40, 10, 30]
plt.plot(x, y, color='#5400ff', label='luchte', marker='>', ms=10)
plt.axis('off')

import matplotlib.pyplot as plt
import numpy as np
def parabola_ploter(a=1,b=1,c=0,title='Parabola plotter'):
    x = np.arange(-10,10,0.01)
    y = a*x**2 + b*x + c
    plt.plot(x,y,label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.show()
    
parabola_plotter()

import matplotlib.pyplot as plt
import numpy as np
 
def circle_plotter(radius=10):
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2 
    plt.contour(X, Y, fxy, levels=[radius**2])
    plt.axis('equal')
    plt.show()
circle_plotter()