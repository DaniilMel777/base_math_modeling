from sympy import sin, cos, pi, exp
from sympy import symbols
x, y, z=symbols('x y z')
expr=(sin(x**2)-exp(-2*x)+cos(pi/x))
expr_new=expr.subs(x, y)
print(expr_new)


expr_num=expr_new.evalf()
print(expr_num)

expr_new=expr.subs(x, x**2)
print(expr_new)

expr=x**3+4*x*y-z
expr_new=expr.subs([(x, 2), (y, 4), (z, 0)])
print(expr_new)

from sympy import sin, cos, pi, exp
from sympy import symbols
from sympy import simplify, expand, factor, trigsimp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
x, y, z=symbols('x y z')
      
expr=16*x**2-17*x-20
solve_expr=solve(expr, x)
print(solve_expr)

expr=Eq(3, 1)
print(expr)

system=[x+y+z-1, x+y+2*z-3, x-2*y+z]
solve_system=linsolve(system, (x, y, z))
print(solve_system)

system=[x**2+x, x-y]
solve_system=nonlinsolve(system, [x, y])
print(solve_system)

expr=16*x**2-17*x-20
solve_expr=solve(expr, x)
print(solve_expr)

expr=Eq(3, 1)
print(expr)

system=[x+y+z-1, x+y+2*z-3, x-2*y+z]
solve_system=linsolve(system, (x, y, z))
print(solve_system)

system=[x**2+x, x-y]
solve_system=nonlinsolve(system, [x, y])
print(solve_system)

system=[x**2+1, y**2+1]
solve_system=nonlinsolve(system, [x, y])
print(solve_system
      
p, o=symbols('p o')
a=1
x=(a*sinh(p))/(cosh(p)-cos(o))
y=(a*sinh(p))/(cosh(p)-cos(o))
p0=float(input('Введите что нить:'))
o1=float(input('Ещё:'))
x0=x.subs([(p,p0),(o,o1)])
y0=y.subs([(p,p0),(o,o1)])
print(x0)
print(y0)


