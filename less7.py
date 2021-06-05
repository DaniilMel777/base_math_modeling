from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs
x, y, z=symbols('x y z')
sol=reduce_abs_inequality(Abs(x-5)-3, '<', x)
print(sol)

sol=reduce_rational_inequalities([[y+2>0]], y)
print(sol)

import sympy
from sympy import solve
from sympy import symbols
from sympy import simplify, expand, factor
import sympy
from sympy import solve
from sympy import symbols
from sympy import simplify, expand, factor
e=0.8
m=9
sol=x**2+x+1/x+1/x**2-4
ex_sol=solve(sol,x)
print(ex_sol)

import sympy
from sympy import solve, solveset
from sympy import symbols
from sympy import simplify, expand, factor
from sympy import sin
E=symbols('E')
e=0.8
m=9
sol=E-e*sin(E)-m
ex_sol=solveset(sol,E)
print(ex_sol)



