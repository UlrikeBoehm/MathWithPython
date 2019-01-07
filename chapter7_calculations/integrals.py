"""
Finding the integrals of functions
"""

# Integral

from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
Integral(k*x,x).doit()

# Definite integral (lower and upper limits are specified)

from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
Integral(k*x,(x,0,2)).doit()
