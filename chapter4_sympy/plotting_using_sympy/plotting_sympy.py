"""
Plotting using SymPy
"""

from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x+3, (x, -5,5), title='A Line', xlabel = 'x', ylabel = '2x+3', show=False)
p.show()
p.save('line.png')