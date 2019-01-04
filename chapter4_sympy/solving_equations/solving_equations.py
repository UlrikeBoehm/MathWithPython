"""

Solving equations - examples

Use: the Anaconda prompt

"""

from sympy import Symbol, solve
x = Symbol('x')
expr = x - 5 - 7
solve(expr)

# Solving Quadratic Equations

# Example 1

from sympy import Symbol, solve
x = Symbol('x')
expr = x**2 + 5*x + 4
solve(expr, dict=True) #(dict=True returns the results as Python dictionary

# Example 2 (solutions are complex)

from sympy import Symbol, solve
x = Symbol('x')
expr = x**2 + x + 1
solve(expr, dict=True) #(dict=True returns the results as Python dictionary

# Solving for one variable in terms of others

# Example 1

from sympy import Symbol, solve
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
solve(expr, x, dict=True)

# Example 2

from sympy import Symbol, solve, pprint
s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr, t, dict=True)
pprint(t_expr)

# Solving a system of linear equations

from sympy import Symbol, solve, pprint
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y -6
expr2 = 3*x + 2*y -12
solve((expr1, expr2), dict=True)