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

# probability density function

from sympy import Symbol, exp, sqrt, pi, Integral
x = Symbol('x')
p = exp(-(x-10)**2/2)/sqrt(2*pi)
Integral(p,(x,11,12)).doit().evalf() # Use evalf() to calculate a numeric value